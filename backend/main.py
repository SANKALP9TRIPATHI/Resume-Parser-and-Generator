from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from resume_parser import parse_resume_file
from resume_generator import generate_resume_pdf

app = FastAPI()

# CORS (adjust if frontend served separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"], # Change to specific domain in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/parse-resume/")
async def parse_resume(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".pdf"):
            return JSONResponse(content={"error": "Only PDF files allowed"}, status_code=400)

        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())

        extracted_fields = parse_resume_file(file_path)
        return extracted_fields
    except Exception as e:
        print("❌ Error:", e)  # <-- This will print the actual error in the terminal
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/generate-resume/")
async def generate_resume(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    summary: str = Form(...),
    skills: str = Form(...),
    experience: str = Form(...),
    education: str = Form(...)
):
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "summary": summary,
        "skills": skills.split(","),
        "experience": experience,
        "education": education
    }

    pdf_path = generate_resume_pdf(data)
    return {"message": "Resume generated", "pdf_path": pdf_path}
