import { useState } from "react";
import { ethers } from "ethers";
import { ShieldCheck, Upload, CheckCircle2 } from "lucide-react";
import "./App.css";

// Update this with the contract address printed from Step 2
const CONTRACT_ADDRESS = "0x5FbDB2315678afecb367f032d93F642f64180aa3";
const CONTRACT_ABI = [
  "function registerMedia(string calldata _pHash, string calldata _metadataUri) external",
  "function verifyMedia(string calldata _pHash) external view returns (bool isVerified, address creator, uint256 timestamp, string memory metadataUri)"
];

// Hardhat's standard default test private key (comes pre-funded with 10,000 test ETH on local node)
const LOCAL_PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80";
const LOCAL_RPC_URL = "http://127.0.0.1:8545";

export default function App() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<string>("");
  const [pHash, setPHash] = useState<string>("");
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      const selectedFile = e.target.files[0];
      setFile(selectedFile);
      setPreview(URL.createObjectURL(selectedFile));

      const formData = new FormData();
      formData.append("file", selectedFile);

      setStatus("Computing Perceptual Hash...");
      const res = await fetch("http://127.0.0.1:8000/api/analyze", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setPHash(data.phash);
      setStatus("Hash computed successfully!");
    }
  };

  const registerOnChain = async () => {
    try {
      setLoading(true);
      setStatus("Connecting to local blockchain node...");
      
      // Connect directly to local Hardhat node without MetaMask
      const provider = new ethers.JsonRpcProvider(LOCAL_RPC_URL);
      const signer = new ethers.Wallet(LOCAL_PRIVATE_KEY, provider);

      const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, signer);

      setStatus("Sending transaction to local ledger...");
      const tx = await contract.registerMedia(pHash, file?.name || "User Upload");
      await tx.wait();

      setStatus("Media successfully registered and immutable on-chain! 🛡️");
    } catch (err: any) {
      console.error(err);
      setStatus("Registration failed: " + (err.reason || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto", padding: "24px", fontFamily: "sans-serif", background: "#0f172a", color: "#f8fafc", borderRadius: "12px", boxShadow: "0 10px 25px rgba(0,0,0,0.5)" }}>
      <h2 style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <ShieldCheck color="#10b981" /> Deepfake Defense - Creator Portal
      </h2>
      <p style={{ color: "#94a3b8", fontSize: "14px" }}>Register original media assets onto the local blockchain ledger.</p>

      <div style={{ border: "2px dashed #334155", padding: "20px", textAlign: "center", borderRadius: "8px", margin: "20px 0", background: "#1e293b" }}>
        <input type="file" onChange={handleFileChange} accept="image/*" style={{ display: "none" }} id="file-upload" />
        <label htmlFor="file-upload" style={{ cursor: "pointer", display: "flex", flexDirection: "column", alignItems: "center", gap: "8px" }}>
          <Upload size={32} color="#38bdf8" />
          <span>Click to upload or drag & drop media file</span>
        </label>
      </div>

      {preview && (
        <div style={{ textAlign: "center", marginBottom: "20px" }}>
          <img src={preview} alt="Preview" style={{ maxHeight: "150px", borderRadius: "6px", border: "1px solid #334155" }} />
        </div>
      )}

      {pHash && (
        <div style={{ background: "#1e293b", padding: "12px", borderRadius: "6px", fontSize: "13px", marginBottom: "20px", wordBreak: "break-all" }}>
          <strong>Generated pHash:</strong> <span style={{ color: "#38bdf8" }}>{pHash}</span>
        </div>
      )}

      <button 
        onClick={registerOnChain} 
        disabled={!pHash || loading}
        style={{ width: "100%", padding: "12px", background: pHash ? "#10b981" : "#475569", color: "#fff", border: "none", borderRadius: "6px", fontWeight: "bold", cursor: pHash ? "pointer" : "not-allowed" }}
      >
        {loading ? "Processing Transaction..." : "Register on Blockchain Ledger"}
      </button>

      {status && (
        <div style={{ marginTop: "16px", padding: "10px", background: "#1e293b", borderRadius: "6px", fontSize: "13px", display: "flex", alignItems: "center", gap: "8px" }}>
          <CheckCircle2 size={16} color="#10b981" /> {status}
        </div>
      )}
    </div>
  );
}