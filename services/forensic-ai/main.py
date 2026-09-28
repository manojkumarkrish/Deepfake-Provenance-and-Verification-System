# from fastapi import FastAPI, UploadFile, File, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import imagehash
# from PIL import Image
# import io
# import os
# import urllib.request
# import cv2
# import numpy as np
# from web3 import Web3
# from transformers import pipeline

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# CASCADE_FILE = "haarcascade_frontalface_default.xml"
# if not os.path.exists(CASCADE_FILE):
#     print("Downloading official Haar Cascade XML for OpenCV...")
#     url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
#     urllib.request.urlretrieve(url, CASCADE_FILE)

# print("Loading SigLIP-2 Deepfake Detector Model...")
# # Switched to a robust SigLIP-2 vision-language model for better real-world generalization
# forensic_pipeline = pipeline("image-classification", model="prithivMLmods/Deepfake-Detect-Siglip2")

# GANACHE_URL = "http://127.0.0.1:8545"
# w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
# CONTRACT_ADDRESS = "0x5fbdb2315678afecb367f032d93F642f64180aa3"
# CONTRACT_ABI_CLEAN = [
#     {
#         "inputs": [{"internalType": "string", "name": "_pHash", "type": "string"}],
#         "name": "verifyMedia",
#         "outputs": [
#             {"internalType": "bool", "name": "isVerified", "type": "bool"},
#             {"internalType": "address", "name": "creator", "type": "address"},
#             {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
#             {"internalType": "string", "name": "metadataUri", "type": "string"}
#         ],
#         "stateMutability": "view",
#         "type": "function"
#     }
# ]
# contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=CONTRACT_ABI_CLEAN)

# def compute_phash(image_bytes: bytes) -> str:
#     image = Image.open(io.BytesIO(image_bytes))
#     return str(imagehash.phash(image))

# def crop_face(image_bytes: bytes) -> Image.Image:
#     nparr = np.frombuffer(image_bytes, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     if img is None:
#         return Image.open(io.BytesIO(image_bytes)).convert("RGB")

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     face_cascade = cv2.CascadeClassifier(CASCADE_FILE)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     if len(faces) > 0:
#         faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
#         x, y, w, h = faces[0]
#         padding = int(0.2 * w)
#         x1 = max(0, x - padding)
#         y1 = max(0, y - padding)
#         x2 = min(img.shape[1], x + w + padding)
#         y2 = min(img.shape[0], y + h + padding)
#         face_crop = img[y1:y2, x1:x2]
#         face_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
#         return Image.fromarray(face_rgb)
    
#     return Image.open(io.BytesIO(image_bytes)).convert("RGB")

# def classify_with_deepfake_model(image_bytes: bytes) -> tuple[bool, float, str, str]:
#     try:
#         processed_image = crop_face(image_bytes)
#         results = forensic_pipeline(processed_image)
        
#         # Debug print to terminal so you can see exact model labels and scores
#         print("Model Raw Output:", results)
        
#         is_deepfake = False
#         confidence = 0.50
#         explanation = "Facial micro-textures, lighting gradients, and pixel distribution conform to organic standards."
#         icon = "🛡️"
        
#         for res in results:
#             label = res['label'].lower()
#             score = res['score']
            
#             # Check for fake/manipulated labels
#             if 'fake' in label or 'deepfake' in label or 'label_0' in label:
#                 if score > 0.85: # Strict threshold to prevent false alarms
#                     is_deepfake = True
#                     confidence = round(float(score), 2)
#                     explanation = "Detected structural spatial anomalies or synthetic generation signatures."
#                     icon = "⚠️"
#                     break
#             elif 'real' in label or 'label_1' in label:
#                 if not is_deepfake:
#                     confidence = round(float(score), 2)
                    
#         return is_deepfake, confidence, explanation, icon
#     except Exception as e:
#         print(f"Inference Error: {e}")
#         return False, 0.50, "Error analyzing image tensor features.", "❓"

# @app.post("/api/analyze")
# async def analyze_image(file: UploadFile = File(...)):
#     try:
#         contents = await file.read()
#         phash = compute_phash(contents)
        
#         is_verified = False
#         creator = "0x0"
#         timestamp = 0
#         metadata = ""
        
#         if w3.is_connected():
#             try:
#                 result = contract.functions.verifyMedia(phash).call()
#                 is_verified, creator, timestamp, metadata = result
#             except: pass

#         if is_verified:
#             return {
#                 "phash": phash, 
#                 "is_authentic": True, 
#                 "is_deepfake": False, 
#                 "confidence": 1.0,
#                 "explanation": "Media asset is cryptographically registered and verified on the blockchain ledger.",
#                 "icon": "✅",
#                 "status": "VERIFIED_AUTHENTIC",
#                 "on_chain_data": {"creator": creator, "timestamp": timestamp, "metadata": metadata}
#             }

#         is_deepfake, confidence, explanation, icon = classify_with_deepfake_model(contents)

#         return {
#             "phash": phash, 
#             "is_authentic": False, 
#             "is_deepfake": is_deepfake, 
#             "confidence": confidence,
#             "explanation": explanation,
#             "icon": icon,
#             "status": "POTENTIAL_DEEPFAKE" if is_deepfake else "UNREGISTERED",
#             "on_chain_data": None
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/")
# def root():
#     return {"status": "Forensic AI Node (SigLIP-2 Engine Active)", "blockchain_connected": w3.is_connected()}


# from fastapi import FastAPI, UploadFile, File, Form, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import imagehash
# from PIL import Image
# import io
# import os
# import urllib.request
# import cv2
# import numpy as np
# from web3 import Web3
# from transformers import pipeline

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# CASCADE_FILE = "haarcascade_frontalface_default.xml"
# if not os.path.exists(CASCADE_FILE):
#     print("Downloading official Haar Cascade XML for OpenCV...")
#     url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
#     urllib.request.urlretrieve(url, CASCADE_FILE)

# print("Loading SigLIP-2 Deepfake Detector Model...")
# forensic_pipeline = pipeline("image-classification", model="prithivMLmods/Deepfake-Detect-Siglip2")

# GANACHE_URL = "http://127.0.0.1:8545"
# w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
# CONTRACT_ADDRESS = "0x5fbdb2315678afecb367f032d93F642f64180aa3"

# CONTRACT_ABI_FULL = [
#     {
#         "inputs": [
#             {"internalType": "string", "name": "_pHash", "type": "string"},
#             {"internalType": "string", "name": "_metadataUri", "type": "string"}
#         ],
#         "name": "registerMedia",
#         "outputs": [],
#         "stateMutability": "nonpayable",
#         "type": "function"
#     },
#     {
#         "inputs": [{"internalType": "string", "name": "_pHash", "type": "string"}],
#         "name": "verifyMedia",
#         "outputs": [
#             {"internalType": "bool", "name": "isVerified", "type": "bool"},
#             {"internalType": "address", "name": "creator", "type": "address"},
#             {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
#             {"internalType": "string", "name": "metadataUri", "type": "string"}
#         ],
#         "stateMutability": "view",
#         "type": "function"
#     }
# ]

# contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=CONTRACT_ABI_FULL)

# def compute_phash(image_bytes: bytes) -> str:
#     image = Image.open(io.BytesIO(image_bytes))
#     return str(imagehash.phash(image))

# def crop_face(image_bytes: bytes) -> Image.Image:
#     nparr = np.frombuffer(image_bytes, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     if img is None:
#         return Image.open(io.BytesIO(image_bytes)).convert("RGB")

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     face_cascade = cv2.CascadeClassifier(CASCADE_FILE)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     if len(faces) > 0:
#         faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
#         x, y, w, h = faces[0]
#         padding = int(0.2 * w)
#         x1 = max(0, x - padding)
#         y1 = max(0, y - padding)
#         x2 = min(img.shape[1], x + w + padding)
#         y2 = min(img.shape[0], y + h + padding)
#         face_crop = img[y1:y2, x1:x2]
#         face_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
#         return Image.fromarray(face_rgb)
    
#     return Image.open(io.BytesIO(image_bytes)).convert("RGB")

# def classify_with_deepfake_model(image_bytes: bytes) -> tuple[bool, float, str, str]:
#     try:
#         processed_image = crop_face(image_bytes)
#         results = forensic_pipeline(processed_image)
        
#         is_deepfake = False
#         confidence = 0.50
#         explanation = "Facial micro-textures, lighting gradients, and pixel distribution conform to organic standards."
#         icon = "🛡️"
        
#         for res in results:
#             label = res['label'].lower()
#             score = res['score']
#             if 'fake' in label or 'deepfake' in label or 'label_0' in label:
#                 if score > 0.85:
#                     is_deepfake = True
#                     confidence = round(float(score), 2)
#                     explanation = "Detected structural spatial anomalies or synthetic generation signatures."
#                     icon = "⚠️"
#                     break
#             elif 'real' in label or 'label_1' in label:
#                 if not is_deepfake:
#                     confidence = round(float(score), 2)
                    
#         return is_deepfake, confidence, explanation, icon
#     except Exception as e:
#         print(f"Inference Error: {e}")
#         return False, 0.50, "Error analyzing image tensor features.", "❓"

# @app.post("/api/analyze")
# async def analyze_image(file: UploadFile = File(...)):
#     try:
#         contents = await file.read()
#         phash = compute_phash(contents)
        
#         is_verified = False
#         creator = "0x0"
#         timestamp = 0
#         metadata = ""
        
#         if w3.is_connected():
#             try:
#                 result = contract.functions.verifyMedia(phash).call()
#                 is_verified, creator, timestamp, metadata = result
#             except: pass

#         if is_verified:
#             return {
#                 "phash": phash, 
#                 "is_authentic": True, 
#                 "is_deepfake": False, 
#                 "confidence": 1.0,
#                 "explanation": "Media asset is cryptographically registered and verified on the blockchain ledger.",
#                 "icon": "✅",
#                 "status": "VERIFIED_AUTHENTIC",
#                 "on_chain_data": {"creator": creator, "timestamp": timestamp, "metadata": metadata}
#             }

#         is_deepfake, confidence, explanation, icon = classify_with_deepfake_model(contents)

#         return {
#             "phash": phash, 
#             "is_authentic": False, 
#             "is_deepfake": is_deepfake, 
#             "confidence": confidence,
#             "explanation": explanation,
#             "icon": icon,
#             "status": "POTENTIAL_DEEPFAKE" if is_deepfake else "UNREGISTERED",
#             "on_chain_data": None
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/api/register")
# async def register_media(file: UploadFile = File(...), metadata_uri: str = Form("ipfs://mock-metadata")):
#     try:
#         contents = await file.read()
#         phash = compute_phash(contents)
        
#         # Step A: Run AI Forensic Gatekeeper to prevent registering deepfakes onto the blockchain ledger
#         is_deepfake, confidence, explanation, icon = classify_with_deepfake_model(contents)
        
#         if is_deepfake:
#             return {
#                 "success": False,
#                 "message": f"Registration rejected: AI forensic scan flagged this asset as a potential deepfake ({round(confidence * 100)}%).",
#                 "confidence": confidence
#             }
            
#         # Step B: Check if already registered on-chain
#         if w3.is_connected():
#             try:
#                 existing = contract.functions.verifyMedia(phash).call()
#                 if existing[0]:
#                     return {"success": False, "message": "Media hash already exists on the blockchain ledger."}
#             except: pass

#             # Step C: Submit Transaction to Hardhat Local Node
#             account = w3.eth.accounts[0]
#             tx_hash = contract.functions.registerMedia(phash, metadata_uri).transact({
#                 'from': account
#             })
#             receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            
#             return {
#                 "success": True,
#                 "phash": phash,
#                 "tx_hash": receipt.transactionHash.hex(),
#                 "message": "Media verified authentic by AI and successfully registered on the blockchain!"
#             }
            
#         return {"success": False, "message": "Blockchain node not connected."}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/")
# def root():
#     return {"status": "Forensic AI Node & Blockchain Registry Active", "blockchain_connected": w3.is_connected()}


from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import imagehash
from PIL import Image
import io
import os
import urllib.request
import cv2
import numpy as np
from web3 import Web3
from transformers import pipeline

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CASCADE_FILE = "haarcascade_frontalface_default.xml"
if not os.path.exists(CASCADE_FILE):
    print("Downloading official Haar Cascade XML for OpenCV...")
    url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
    urllib.request.urlretrieve(url, CASCADE_FILE)

print("Loading SigLIP-2 Deepfake Detector Model...")
forensic_pipeline = pipeline("image-classification", model="prithivMLmods/Deepfake-Detect-Siglip2")

GANACHE_URL = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))
CONTRACT_ADDRESS = "0x5fbdb2315678afecb367f032d93F642f64180aa3"

CONTRACT_ABI_FULL = [
    {
        "inputs": [
            {"internalType": "string", "name": "_pHash", "type": "string"},
            {"internalType": "string", "name": "_metadataUri", "type": "string"}
        ],
        "name": "registerMedia",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [{"internalType": "string", "name": "_pHash", "type": "string"}],
        "name": "verifyMedia",
        "outputs": [
            {"internalType": "bool", "name": "isVerified", "type": "bool"},
            {"internalType": "address", "name": "creator", "type": "address"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"internalType": "string", "name": "metadataUri", "type": "string"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=CONTRACT_ABI_FULL)

def compute_phash(image_bytes: bytes) -> str:
    image = Image.open(io.BytesIO(image_bytes))
    return str(imagehash.phash(image))

def crop_face(image_bytes: bytes) -> Image.Image:
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        return Image.open(io.BytesIO(image_bytes)).convert("RGB")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(CASCADE_FILE)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
        x, y, w, h = faces[0]
        padding = int(0.2 * w)
        x1 = max(0, x - padding)
        y1 = max(0, y - padding)
        x2 = min(img.shape[1], x + w + padding)
        y2 = min(img.shape[0], y + h + padding)
        face_crop = img[y1:y2, x1:x2]
        face_rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)
        return Image.fromarray(face_rgb)
    
    return Image.open(io.BytesIO(image_bytes)).convert("RGB")

def classify_with_deepfake_model(image_bytes: bytes) -> tuple[bool, float, str, str]:
    try:
        processed_image = crop_face(image_bytes)
        results = forensic_pipeline(processed_image)
        
        is_deepfake = False
        confidence = 0.50
        explanation = "Facial micro-textures, lighting gradients, and pixel distribution conform to organic standards."
        icon = "🛡️"
        
        for res in results:
            label = res['label'].lower()
            score = res['score']
            if 'fake' in label or 'deepfake' in label or 'label_0' in label:
                if score > 0.85:
                    is_deepfake = True
                    confidence = round(float(score), 2)
                    explanation = "Detected structural spatial anomalies or synthetic generation signatures."
                    icon = "⚠️"
                    break
            elif 'real' in label or 'label_1' in label:
                if not is_deepfake:
                    confidence = round(float(score), 2)
                    
        return is_deepfake, confidence, explanation, icon
    except Exception as e:
        print(f"Inference Error: {e}")
        return False, 0.50, "Error analyzing image tensor features.", "❓"

@app.post("/api/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        phash = compute_phash(contents)
        
        is_verified = False
        creator = "0x0"
        timestamp = 0
        metadata = ""
        
        if w3.is_connected():
            try:
                result = contract.functions.verifyMedia(phash).call()
                is_verified, creator, timestamp, metadata = result
            except: pass

        if is_verified:
            return {
                "phash": phash, 
                "is_authentic": True, 
                "is_deepfake": False, 
                "confidence": 1.0,
                "explanation": "Media asset is cryptographically registered and verified on the blockchain ledger.",
                "icon": "✅",
                "status": "VERIFIED_AUTHENTIC",
                "on_chain_data": {"creator": creator, "timestamp": timestamp, "metadata": metadata}
            }

        is_deepfake, confidence, explanation, icon = classify_with_deepfake_model(contents)

        return {
            "phash": phash, 
            "is_authentic": False, 
            "is_deepfake": is_deepfake, 
            "confidence": confidence,
            "explanation": explanation,
            "icon": icon,
            "status": "POTENTIAL_DEEPFAKE" if is_deepfake else "UNREGISTERED",
            "on_chain_data": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/register")
async def register_media(file: UploadFile = File(...), metadata_uri: str = Form("ipfs://mock-metadata")):
    try:
        contents = await file.read()
        phash = compute_phash(contents)
        
        # Step A: Run AI Forensic Gatekeeper to prevent registering deepfakes onto the blockchain ledger
        is_deepfake, confidence, explanation, icon = classify_with_deepfake_model(contents)
        
        if is_deepfake:
            return {
                "success": False,
                "message": f"Registration rejected: AI forensic scan flagged this asset as a potential deepfake ({round(confidence * 100)}%).",
                "confidence": confidence
            }
            
        # Step B: Check if already registered on-chain
        if w3.is_connected():
            try:
                existing = contract.functions.verifyMedia(phash).call()
                if existing[0]:
                    return {"success": False, "message": "Media hash already exists on the blockchain ledger."}
            except: pass

            # Step C: Submit Transaction to Hardhat Local Node
            account = w3.eth.accounts[0]
            tx_hash = contract.functions.registerMedia(phash, metadata_uri).transact({
                'from': account
            })
            receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
            
            return {
                "success": True,
                "phash": phash,
                "tx_hash": receipt.transactionHash.hex(),
                "message": "Media verified authentic by AI and successfully registered on the blockchain!"
            }
            
        return {"success": False, "message": "Blockchain node not connected."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"status": "Forensic AI Node & Blockchain Registry Active", "blockchain_connected": w3.is_connected()}