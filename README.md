# 📝 Resume Parser & Generator Web App

An offline-capable, full-stack web application to **generate resumes from structured form data** and **parse uploaded PDF resumes** using Gemini API for smart extraction.

---

## 🚀 Features

- ✅ **Resume Generator**: Fill out a form and download a beautiful PDF resume.
- 📄 **Resume Parser**: Upload an existing PDF resume to extract structured data (Name, Email, Skills, etc.).
- 🔗 Local-only (no cloud storage) with privacy-first design.
- 🤖 Uses **Gemini API** (Google PaLM) for intelligent resume field extraction.
- 🌐 Built with **FastAPI** (Python backend) + **HTML/CSS/JS** frontend.

---

## 🛠️ Tech Stack

| Component       | Technology              |
|----------------|--------------------------|
| Backend         | FastAPI, Python, WeasyPrint |
| NLP Parsing     | Gemini 2.0 Flash API (via `google.generativeai`) |
| PDF Parsing     | PyMuPDF (`fitz`)         |
| Frontend        | HTML, CSS (Tailwind-style), JavaScript |
| Storage         | Local file system        |

---


