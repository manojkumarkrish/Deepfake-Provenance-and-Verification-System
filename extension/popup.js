document.addEventListener("DOMContentLoaded", async () => {
  const statusEl = document.getElementById("ai-status");
  try {
    const res = await fetch("http://127.0.0.1:8000/docs");
    if (res.ok) {
      statusEl.innerHTML = '<span style="color:#10b981">● Active</span>';
    } else {
      statusEl.innerHTML = '<span style="color:#f59e0b">● Degrading</span>';
    }
  } catch (e) {
    statusEl.innerHTML = '<span style="color:#ef4444">● Offline</span>';
  }
});