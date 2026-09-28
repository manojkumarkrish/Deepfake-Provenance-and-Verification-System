const API_URL = "http://127.0.0.1:8000/api/analyze";
const processedImages = new WeakSet();

async function analyzeImage(imgElement) {
  if (processedImages.has(imgElement)) return;
  if (imgElement.naturalWidth < 120 || imgElement.naturalHeight < 120) return;

  processedImages.add(imgElement);

  try {
    const response = await fetch(imgElement.src, { mode: "cors" });
    const blob = await response.blob();

    const formData = new FormData();
    formData.append("file", blob, "scanned_image.jpg");

    const apiResponse = await fetch(API_URL, {
      method: "POST",
      body: formData,
    });

    if (!apiResponse.ok) return;

    const data = await apiResponse.json();
    injectBadge(imgElement, data);
  } catch (error) {
    // Cross-origin restriction or server offline
  }
}

function injectBadge(imgElement, forensicData) {
  const wrapper = document.createElement("div");
  wrapper.className = "df-scanner-wrapper";
  wrapper.style.position = "relative";
  wrapper.style.display = "inline-block";
  
  const badge = document.createElement("div");
  badge.className = "df-badge";
  badge.style.position = "absolute";
  badge.style.top = "8px";
  badge.style.left = "8px";
  badge.style.padding = "4px 8px";
  badge.style.borderRadius = "6px";
  badge.style.fontSize = "11px";
  badge.style.fontWeight = "bold";
  badge.style.zIndex = "999999";
  badge.style.color = "#ffffff";
  badge.style.cursor = "pointer";
  badge.style.boxShadow = "0 2px 4px rgba(0,0,0,0.3)";

  const confPercent = Math.round(forensicData.confidence * 100);
  badge.title = `Explanation: ${forensicData.explanation}`;

  if (forensicData.status === "VERIFIED_AUTHENTIC") {
    badge.style.backgroundColor = "#10b981"; // Green
    badge.innerHTML = `${forensicData.icon} Verified (${confPercent}%)`;
  } else if (forensicData.is_deepfake) {
    badge.style.backgroundColor = "#ef4444"; // Red
    badge.innerHTML = `${forensicData.icon} Deepfake (${confPercent}%)`;
  } else {
    badge.style.backgroundColor = "#6b7280"; // Gray
    badge.innerHTML = `${forensicData.icon} Unregistered`;
  }

  if (imgElement.parentNode && !imgElement.parentNode.classList.contains("df-scanner-wrapper")) {
    imgElement.parentNode.insertBefore(wrapper, imgElement);
    wrapper.appendChild(imgElement);
    wrapper.appendChild(badge);
  }
}

function scanDOM() {
  const images = document.querySelectorAll("img");
  images.forEach((img) => {
    if (img.complete) {
      analyzeImage(img);
    } else {
      img.addEventListener("load", () => analyzeImage(img), { once: true });
    }
  });
}

scanDOM();
const observer = new MutationObserver(() => scanDOM());
observer.observe(document.body, { childList: true, subtree: true });