
# 🛡️ Blockchain-Enabled Deepfake Defense & Media Provenance System

> An end-to-end cybersecurity and content verification framework designed to combat generative synthetic media through **AI-powered deepfake detection, computer vision, Explainable AI (XAI), browser-level inspection, and blockchain-based media provenance**.

---

## 📌 Overview

The **Blockchain-Enabled Deepfake Defense & Media Provenance System** is an end-to-end cybersecurity framework designed to detect, analyze, verify, and trace potentially manipulated or AI-generated media.

The system combines:

- 🌐 **Real-time browser inspection**
- 🤖 **AI-powered deepfake detection**
- 👁️ **Computer vision preprocessing**
- 🧠 **Vision-language AI forensics**
- 🔐 **Blockchain-based media provenance**
- 🧾 **Perceptual hash (pHash) verification**
- 💡 **Explainable AI (XAI) security indicators**

The system operates across three major tiers:

```text
┌──────────────────────────────────────────────────────────────┐
│                         CLIENT TIER                          │
│                                                              │
│  Google Chrome Extension (Manifest V3)                      │
│  DOM Monitoring → Image Detection → XAI Security Badges      │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                    APPLICATION SERVER TIER                   │
│                                                              │
│  FastAPI → OpenCV → Face Isolation → SigLIP-2 AI Forensics  │
│                                                              │
└──────────────────────────────┬───────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                    DECENTRALIZED LEDGER TIER                 │
│                                                              │
│  Solidity → Hardhat → Ethereum-Compatible Network → Polygon │
│                                                              │
│  pHash + Creator Metadata → Immutable Provenance             │
└──────────────────────────────────────────────────────────────┘
````

---

# ✨ Key Features

* 🔍 **Real-time Deepfake Detection**
* 🌐 **Chrome Extension-based Web Inspection**
* 🧬 **AI-powered Synthetic Media Analysis**
* 👤 **OpenCV Face Detection and Isolation**
* 🧠 **SigLIP-2 Vision-Language Classification**
* 🔐 **Blockchain-backed Media Provenance**
* #️⃣ **Perceptual Hash (pHash) Verification**
* 🧾 **Creator Metadata Registration**
* 🚫 **Pre-flight AI Validation**
* 💡 **Explainable AI Security Badges**
* 📊 **Interactive XAI Verification Modal**
* ⚡ **FastAPI REST Backend**
* ⚛️ **React.js Creator Dashboard**
* ⛓️ **Ethereum-Compatible Smart Contract**
* 🧪 **Hardhat Local Blockchain Development**
* 🟣 **Polygon Layer-2 Deployment Architecture**

---

# 🏗️ System Architecture

The system consists of three primary functional tiers.

## 1. Client Tier

The client tier is implemented as a **Google Chrome Extension using Manifest V3**.

It continuously monitors webpage DOM structures and detects images dynamically loaded onto webpages.

### Responsibilities

* Monitor webpage DOM changes
* Detect newly added images
* Filter images based on size
* Extract image information
* Send images to the backend
* Display verification results
* Inject XAI security badges
* Display detailed verification information

### Technologies

* JavaScript
* Chrome Extension Manifest V3
* `MutationObserver`
* `WeakSet`
* HTML
* CSS

---

## 2. Application Server Tier

The application server is implemented using **Python FastAPI**.

It acts as the central processing layer between the Chrome extension, AI forensic engine, and blockchain network.

### Responsibilities

* Receive images from the browser extension
* Perform image preprocessing
* Detect and isolate faces
* Run AI forensic analysis
* Check blockchain provenance
* Register verified media
* Return verification results to the extension

### Technologies

* Python 3.10+
* FastAPI
* Uvicorn
* OpenCV
* Pillow
* NumPy
* ImageHash
* Web3.py
* Hugging Face Transformers
* PyTorch

---

## 3. Decentralized Ledger Tier

The blockchain tier provides immutable provenance for verified media.

The system uses an Ethereum-compatible Solidity smart contract called:

```text
MediaRegistry.sol
```

The contract can be deployed on:

* Hardhat local development network
* Ethereum-compatible networks
* Polygon Layer-2 architecture

### Blockchain Responsibilities

* Store perceptual hashes
* Store creator metadata
* Verify previously registered media
* Maintain immutable provenance records
* Prevent unauthorized modification of registered records

---

# 🧩 Technology Stack

## Frontend & Browser Extension

| Technology         | Purpose                         |
| ------------------ | ------------------------------- |
| React.js           | Creator dashboard               |
| Vite               | Frontend development/build tool |
| Tailwind CSS       | UI styling                      |
| JavaScript         | Extension logic                 |
| Chrome Manifest V3 | Browser extension architecture  |
| MutationObserver   | DOM monitoring                  |
| WeakSet            | Tracking processed images       |

---

## Backend & Computer Vision

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python 3.10+ | Backend programming language        |
| FastAPI      | REST API framework                  |
| Uvicorn      | ASGI server                         |
| OpenCV       | Image processing and face detection |
| Pillow       | Image manipulation                  |
| NumPy        | Numerical/image processing          |
| ImageHash    | Perceptual hash generation          |
| Web3.py      | Blockchain communication            |

---

## AI Forensic Engine

| Technology                              | Purpose                        |
| --------------------------------------- | ------------------------------ |
| Hugging Face Transformers               | AI model inference             |
| PyTorch                                 | Deep learning framework        |
| SigLIP-2                                | Vision-language classification |
| `prithivMLmods/Deepfake-Detect-Siglip2` | Deepfake forensic model        |

---

## Blockchain & Web3

| Technology                  | Purpose                                |
| --------------------------- | -------------------------------------- |
| Solidity `^0.8.0`           | Smart contract development             |
| Hardhat                     | Local Ethereum development environment |
| Web3.py                     | Python blockchain interaction          |
| Ethereum-compatible network | Decentralized ledger                   |
| Polygon Layer-2             | Scalable blockchain deployment         |

---

# 📂 Repository Structure

```text
Blockchain-Deepfake-Defense/
│
├── blockchain/
│   ├── contracts/
│   │   └── MediaRegistry.sol
│   │
│   ├── scripts/
│   │   ├── deploy.ts
│   │   └── test.ts
│   │
│   └── hardhat.config.ts
│
├── extension/
│   ├── content.js
│   ├── manifest.json
│   ├── popup.html
│   ├── popup.js
│   └── styles.css
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── ...
│   │
│   └── package.json
│
├── services/
│   └── forensic-ai/
│
├── main.py
│
├── README.md
│
└── package.json
```

---

# 🔄 System Workflow

The complete system follows the pipeline:

```text
                    ┌───────────────────┐
                    │    Web Browser    │
                    │   Google Chrome   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Chrome Extension  │
                    │    Manifest V3    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  DOM Monitoring   │
                    │ MutationObserver  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Image Detection  │
                    │      ≥ 120px      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   FastAPI Server  │
                    │     /api/analyze  │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
       ┌──────────────────┐      ┌────────────────────┐
       │    Blockchain    │      │  Computer Vision   │
       │ Provenance Check │      │      OpenCV        │
       └────────┬─────────┘      └─────────┬──────────┘
                │                          │
                ▼                          ▼
       ┌──────────────────┐      ┌────────────────────┐
       │ verifyMedia()    │      │ Face Detection &   │
       │ Smart Contract   │      │ Face Isolation     │
       └────────┬─────────┘      └─────────┬──────────┘
                │                          │
                │                          ▼
                │                 ┌────────────────────┐
                │                 │     SigLIP-2       │
                │                 │   AI Forensics     │
                │                 └─────────┬──────────┘
                │                           │
                └────────────┬──────────────┘
                             │
                             ▼
                   ┌──────────────────────┐
                   │ Verification Result  │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │    XAI Security      │
                   │        Badge         │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │    XAI Explanation   │
                   │        Modal         │
                   └──────────────────────┘
```

---

# 🔍 Real-Time Web Browsing Workflow

When a user browses the web, the Chrome extension continuously monitors the webpage.

## Step 1 — DOM Monitoring

The extension uses JavaScript `MutationObserver` to detect changes in the webpage DOM.

```javascript
MutationObserver
        │
        ▼
New DOM Elements
        │
        ▼
Detect Images
```

This allows the extension to identify images that are dynamically loaded after the webpage initially renders.

---

## Step 2 — Image Filtering

Images are inspected based on their dimensions.

Images smaller than the configured threshold are ignored.

```text
Image Width >= 120px
        │
        ▼
     Process
```

This reduces unnecessary processing of small icons, thumbnails, and decorative elements.

---

## Step 3 — Image Extraction

The extension extracts the image data and sends it to the backend.

```text
Chrome Extension
       │
       ▼
Image Binary
       │
       ▼
POST /api/analyze
       │
       ▼
FastAPI Backend
```

---

# 🧠 AI Forensic Analysis Pipeline

The backend performs multiple processing stages before generating the final verification result.

```text
Input Image
     │
     ▼
Image Preprocessing
     │
     ▼
OpenCV Face Detection
     │
     ▼
Face Isolation
     │
     ▼
Image Normalization
     │
     ▼
SigLIP-2 Model
     │
     ▼
Vision-Language Classification
     │
     ▼
Forensic Result
```

The system uses:

```text
prithivMLmods/Deepfake-Detect-Siglip2
```

for vision-language based deepfake classification.

---

# 👤 Computer Vision Processing

OpenCV is used as the computer vision preprocessing layer.

The system uses:

```text
haarcascade_frontalface_default.xml
```

for face detection.

### Processing

```text
Original Image
      │
      ▼
OpenCV
      │
      ▼
Face Detection
      │
      ▼
Face Bounding Box
      │
      ▼
Face Isolation
      │
      ▼
AI Forensic Analysis
```

This allows the forensic engine to focus on relevant facial regions when analyzing potentially manipulated media.

---

# ⛓️ Blockchain Provenance Verification

The blockchain layer provides an additional source of media provenance.

The backend communicates with the smart contract:

```text
MediaRegistry.sol
```

The contract maintains records associated with registered media.

A media record can contain information such as:

```text
┌─────────────────────────────┐
│      Media Registry         │
├─────────────────────────────┤
│ Perceptual Hash (pHash)     │
│ Creator Metadata            │
│ Registration Information    │
│ Blockchain Record           │
└─────────────────────────────┘
```

---

# 🔐 Perceptual Hash (pHash)

The system uses **perceptual hashing** to generate a compact representation of an image.

Unlike a traditional cryptographic hash, a perceptual hash is designed to help identify visually similar images even when minor modifications have been made.

Example:

```text
Original Image
      │
      ▼
   pHash
      │
      ▼
Blockchain Registry
```

The pHash can later be used during media verification.

---

# 🚦 Pre-Flight Blockchain Registration

Before registering media on the blockchain, the system performs an AI forensic validation.

```text
Creator Uploads Media
        │
        ▼
     /api/register
        │
        ▼
AI Forensic Gatekeeper
        │
        ▼
Deepfake Analysis
        │
        ├───────────────┐
        │               │
        ▼               ▼
   Synthetic        Authentic
     Media            Media
        │               │
        ▼               ▼
 Registration       Generate
   Rejected           pHash
                        │
                        ▼
                Creator Metadata
                        │
                        ▼
                 Smart Contract
                        │
                        ▼
                Blockchain Ledger
```

---

## 🚫 Synthetic Media

If the forensic engine determines that the media should not pass the configured authenticity gate, blockchain registration is rejected.

```text
Synthetic / Manipulated Media
             │
             ▼
      AI Forensic Gate
             │
             ▼
      Registration Rejected
             │
             ▼
       No Ledger Entry
```

This helps prevent questionable media from being added to the provenance registry.

---

## ✅ Authentic / Accepted Media

If the media passes the configured forensic validation:

```text
Media
 │
 ▼
AI Validation
 │
 ▼
Accepted
 │
 ├──► Generate pHash
 │
 ├──► Collect Creator Metadata
 │
 └──► Submit Blockchain Transaction
              │
              ▼
       MediaRegistry.sol
              │
              ▼
      Immutable Record
```

---

# 💡 Explainable AI (XAI)

Instead of providing only a raw classification result, the Chrome extension presents security information directly on the webpage.

Example states:

```text
🟢 VERIFIED

🔴 POTENTIAL DEEPFAKE

🟡 UNVERIFIED
```

The user can interact with the security badge to view additional forensic information.

Example:

```text
┌────────────────────────────────────┐
│       🛡️ Media Security Report     │
├────────────────────────────────────┤
│ Status: Potentially Synthetic      │
│                                    │
│ AI Analysis: Completed             │
│ Blockchain: Not Registered         │
│ Face Analysis: Completed           │
│                                    │
│ Explanation:                       │
│ Forensic analysis identified       │
│ indicators requiring review.       │
└────────────────────────────────────┘
```

---

# 🧑‍💻 Creator Dashboard

The React-based creator dashboard provides an interface for media registration and provenance management.

Potential workflow:

```text
Creator Dashboard
       │
       ▼
Upload Media
       │
       ▼
AI Forensic Validation
       │
       ▼
pHash Generation
       │
       ▼
Blockchain Registration
       │
       ▼
Provenance Record
```

---

# 🚀 Installation & Setup

## Prerequisites

Before running the project, install the following:

* Python 3.10 or higher
* Node.js
* npm
* Google Chrome
* Git

### Recommended

```text
Python 3.10+
Node.js 18+
npm
Google Chrome
Git
```

> **Windows users:** During Python installation, make sure **"Add Python to PATH"** is enabled.

---

# ⚙️ Backend Setup

Navigate to the project root:

```bash
cd Blockchain-Deepfake-Defense
```

---

## Create Python Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## Install Backend Dependencies

```bash
pip install fastapi uvicorn imagehash pillow opencv-contrib-python numpy web3 transformers torch
```

---

# ⛓️ Start the Local Blockchain

Open a **new terminal**.

Navigate to the project directory:

```bash
cd Blockchain-Deepfake-Defense
```

Install Node dependencies:

```bash
npm install
```

Start the Hardhat development node:

```bash
npx hardhat node
```

The local blockchain will be available at:

```text
http://127.0.0.1:8545
```

Keep this terminal running.

---

# 🚀 Start the FastAPI Backend

Return to the terminal containing the Python virtual environment.

Run:

```bash
uvicorn main:app --reload --port 8000
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 FastAPI Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to test endpoints such as:

```text
/api/analyze
/api/register
```

---

# 🌐 Load the Chrome Extension

Open Google Chrome.

Navigate to:

```text
chrome://extensions/
```

### Steps

1. Enable **Developer mode**.
2. Click **Load unpacked**.
3. Select the project's `extension` directory.
4. The extension will be added to Chrome.
5. Pin the extension to the toolbar if required.

Example:

```text
Chrome
  │
  ▼
chrome://extensions/
  │
  ▼
Developer Mode
  │
  ▼
Load Unpacked
  │
  ▼
Select:
extension/
```

---

# 🧪 Running the Complete System

The project requires multiple components to run simultaneously.

## Terminal 1 — Backend

```bash
venv\Scripts\activate

uvicorn main:app --reload --port 8000
```

---

## Terminal 2 — Blockchain

```bash
npm install

npx hardhat node
```

---

## Browser — Chrome Extension

```text
chrome://extensions/
        │
        ▼
Developer Mode
        │
        ▼
Load Unpacked
        │
        ▼
extension/
```

---

# 🔄 Complete End-to-End Example

Suppose a user visits a webpage containing an image.

```text
1. User opens webpage
          │
          ▼
2. Chrome Extension detects image
          │
          ▼
3. MutationObserver identifies image
          │
          ▼
4. Image size is checked
          │
          ▼
5. Image is sent to FastAPI
          │
          ▼
6. Backend checks blockchain provenance
          │
          ▼
7. OpenCV detects/isolate faces
          │
          ▼
8. SigLIP-2 performs AI forensic analysis
          │
          ▼
9. Backend generates verification result
          │
          ▼
10. Extension receives result
          │
          ▼
11. XAI security badge is displayed
          │
          ▼
12. User can inspect the XAI explanation
```

---

# 🧱 Smart Contract Architecture

The blockchain component is based around:

```text
MediaRegistry.sol
```

The smart contract provides functionality for:

* Media registration
* pHash storage
* Creator metadata storage
* Media verification
* Provenance lookup

Conceptual architecture:

```text
                    MediaRegistry.sol
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       Register Media            Verify Media
              │                         │
              ▼                         ▼
         Store pHash              Search pHash
              │                         │
              ▼                         ▼
       Creator Metadata           Provenance
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                    Blockchain Ledger
```

---

# 🛡️ Security Architecture

The system uses multiple security layers.

```text
┌──────────────────────────────────────────┐
│             Browser Layer                │
│                                          │
│ Chrome Extension                         │
│ DOM Monitoring                           │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│             AI Analysis Layer            │
│                                          │
│ OpenCV + Face Detection + SigLIP-2      │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│          Provenance Verification         │
│                                          │
│ pHash + Smart Contract + Blockchain     │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│             XAI Layer                    │
│                                          │
│ Security Badge + Explanation Modal      │
└──────────────────────────────────────────┘
```

---

# 📊 API Architecture

The FastAPI backend exposes endpoints for media analysis and registration.

## Analyze Media

```http
POST /api/analyze
```

### Purpose

Analyzes an image using:

* Blockchain provenance verification
* OpenCV preprocessing
* Face detection
* AI forensic classification

---

## Register Media

```http
POST /api/register
```

### Purpose

Validates uploaded media before registering its provenance on the blockchain.

```text
Upload
  │
  ▼
AI Validation
  │
  ├── Rejected → Stop
  │
  └── Accepted
          │
          ▼
       pHash
          │
          ▼
   Creator Metadata
          │
          ▼
  Smart Contract
          │
          ▼
 Blockchain Record
```

---

# 🧠 Why Combine AI and Blockchain?

AI and blockchain solve different parts of the media authenticity problem.

| Technology       | Primary Role                                      |
| ---------------- | ------------------------------------------------- |
| AI               | Detect potentially synthetic or manipulated media |
| Computer Vision  | Extract and preprocess visual information         |
| Blockchain       | Maintain tamper-resistant provenance records      |
| pHash            | Identify visually similar media                   |
| Chrome Extension | Perform real-time browser-level inspection        |
| XAI              | Explain verification results to users             |

The combination creates a multi-layered media verification architecture.

---

# 🎯 Core Objectives

The project aims to:

1. Detect potentially AI-generated or manipulated media.
2. Provide real-time protection while users browse the web.
3. Analyze facial regions using computer vision.
4. Use vision-language AI for forensic classification.
5. Verify whether media has registered provenance.
6. Prevent rejected media from entering the provenance registry.
7. Store accepted media provenance on-chain.
8. Provide explainable security information to users.
9. Create a scalable architecture suitable for Ethereum-compatible networks.
10. Support future deployment using Polygon Layer-2 infrastructure.

---

# 🔮 Future Enhancements

Potential future improvements include:

* 📹 Video deepfake detection
* 🎙️ Audio deepfake detection
* 🧠 Multimodal audio-video analysis
* 🔗 IPFS-based decentralized media storage
* 🟣 Polygon production deployment
* 📱 Mobile application integration
* 🔐 Digital signatures for creators
* 👤 Decentralized creator identity
* 📈 Advanced provenance analytics
* 🧪 Automated forensic benchmarking
* ⚡ GPU-accelerated inference
* 🌍 Multi-language XAI explanations
* ☁️ Cloud deployment
* 🔄 Real-time provenance synchronization
* 🧩 Browser support beyond Chrome

---

# ⚠️ Limitations

Deepfake detection is probabilistic and should not be treated as absolute proof of authenticity.

Potential limitations include:

* AI detection models can produce false positives.
* AI detection models can produce false negatives.
* Image compression can affect forensic analysis.
* Very small images may not contain sufficient visual information.
* Blockchain registration proves the existence of a recorded provenance entry, but does not by itself prove that the underlying real-world event depicted by the media occurred.
* Perceptual hashes can help identify visually similar media but should not be treated as cryptographic proof of content authenticity.
* Model performance can vary across different image-generation techniques and manipulation methods.

---

# 🔒 Security Considerations

For production deployment, the following should be considered:

* Never expose private blockchain keys in frontend code.
* Use environment variables for sensitive configuration.
* Restrict API access where appropriate.
* Validate uploaded files.
* Limit maximum upload size.
* Sanitize metadata.
* Apply rate limiting.
* Use HTTPS in production.
* Use secure CORS configuration.
* Protect blockchain RPC credentials.
* Monitor AI inference resources.
* Validate smart-contract inputs.
* Perform smart-contract security testing before deployment.

---

# 🧪 Development Environment

### Recommended Development Stack

```text
Operating System
├── Windows / Linux / macOS
│
├── Python
│   └── 3.10+
│
├── Node.js
│   └── npm
│
├── Blockchain
│   └── Hardhat
│
├── Backend
│   └── FastAPI + Uvicorn
│
├── AI
│   ├── PyTorch
│   ├── Transformers
│   └── SigLIP-2
│
├── Computer Vision
│   └── OpenCV
│
├── Frontend
│   ├── React
│   ├── Vite
│   └── Tailwind CSS
│
└── Browser
    └── Google Chrome
```

---

# 📌 Quick Start

For a quick local setup:

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd Blockchain-Deepfake-Defense
```

### 2. Create Python environment

```bash
python -m venv venv
```

### 3. Activate environment

```bash
venv\Scripts\activate
```

### 4. Install Python dependencies

```bash
python -m pip install --upgrade pip

pip install fastapi uvicorn imagehash pillow opencv-contrib-python numpy web3 transformers torch
```

### 5. Install Node dependencies

```bash
npm install
```

### 6. Start Hardhat

```bash
npx hardhat node
```

### 7. Start FastAPI

Open another terminal:

```bash
venv\Scripts\activate

uvicorn main:app --reload --port 8000
```

### 8. Open API documentation

```text
http://127.0.0.1:8000/docs
```

### 9. Load Chrome Extension

```text
chrome://extensions/
```

Enable **Developer Mode → Load Unpacked → Select `extension/`**.

---

# 📜 Project Workflow Summary

```text
                  USER
                   │
                   ▼
             WEB BROWSING
                   │
                   ▼
        ┌─────────────────────┐
        │ Chrome Extension    │
        │ Manifest V3         │
        └──────────┬──────────┘
                   │
                   ▼
             IMAGE FOUND
                   │
                   ▼
          ┌─────────────────┐
          │ FastAPI Backend │
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          │                  │
          ▼                  ▼
      Blockchain          OpenCV
      Verification        Processing
          │                  │
          │                  ▼
          │             Face Isolation
          │                  │
          │                  ▼
          │              SigLIP-2
          │                  │
          └────────┬─────────┘
                   │
                   ▼
            FORENSIC RESULT
                   │
                   ▼
             XAI SECURITY
                BADGE
                   │
                   ▼
            USER EXPLANATION
```

---

# 🏆 Project Highlights

| Component               | Implementation          |
| ----------------------- | ----------------------- |
| Browser Security        | Chrome Extension        |
| Browser Architecture    | Manifest V3             |
| DOM Monitoring          | MutationObserver        |
| Frontend                | React.js + Vite         |
| UI Styling              | Tailwind CSS            |
| Backend                 | FastAPI                 |
| Server                  | Uvicorn                 |
| Computer Vision         | OpenCV                  |
| Face Detection          | Haar Cascade            |
| Image Processing        | Pillow + NumPy          |
| Perceptual Hashing      | ImageHash               |
| AI Framework            | PyTorch                 |
| AI Platform             | Hugging Face            |
| AI Model                | Deepfake-Detect-Siglip2 |
| Blockchain Language     | Solidity                |
| Blockchain Framework    | Hardhat                 |
| Web3 Interface          | Web3.py                 |
| Local Blockchain        | Hardhat Node            |
| Production Architecture | Polygon Layer-2         |
| Explanation Layer       | XAI                     |
| Provenance              | Blockchain Ledger       |

---

# 👨‍💻 Project Structure at a Glance

```text
                    PROJECT
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
   EXTENSION       BACKEND        BLOCKCHAIN
        │              │              │
        ▼              ▼              ▼
    Chrome MV3       FastAPI       Solidity
        │              │              │
        ▼              ▼              ▼
 MutationObserver    OpenCV        Hardhat
        │              │              │
        │              ▼              ▼
        │          SigLIP-2       MediaRegistry
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                  VERIFICATION
                       │
                       ▼
                     XAI
                       │
                       ▼
               MEDIA PROVENANCE
```

---
