document.addEventListener("DOMContentLoaded", () => {
  const resumeForm = document.getElementById("resumeForm");
  const uploadForm = document.getElementById("uploadForm");

  if (resumeForm) {
    resumeForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(resumeForm);

      const res = await fetch("http://localhost:8000/generate-resume", {
        method: "POST",
        body: formData  // ✅ send FormData directly
      });

      if (res.ok) {
        const blob = await res.blob();
        const link = document.createElement("a");
        link.href = window.URL.createObjectURL(blob);
        link.download = "generated_resume.pdf";
        link.click();
        document.getElementById("generateStatus").textContent = "✅ Resume downloaded!";
      } else {
        const errorText = await res.text();
        document.getElementById("generateStatus").textContent = "❌ Failed to generate: " + errorText;
        console.error("Error:", errorText);
      }
    }); // <-- Missing closing brace and parenthesis added here
  }

  if (uploadForm) {
    uploadForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const formData = new FormData(uploadForm);

      const res = await fetch("http://localhost:8000/parse-resume", {
        method: "POST",
        body: formData
      });

      const output = document.getElementById("parsedOutput");
      if (res.ok) {
        const data = await res.json();
        output.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
      } else {
        output.textContent = "❌ Failed to parse resume.";
      }
    });
  }
}); // <-- Closing the DOMContentLoaded event listener