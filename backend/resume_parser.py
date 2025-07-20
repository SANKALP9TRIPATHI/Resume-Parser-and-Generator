from pdf_utils import extract_text_from_pdf
from gemini_api import generate_response

PROMPT_PATH = "C:\\Users\\Home\\Downloads\\Documents\\Resume_Parser\\models\\prompts\\extract_resume.gemini.txt"


def parse_resume_file(pdf_path: str) -> dict:
    with open(PROMPT_PATH, "r") as f:
        prompt_template = f.read()

    pdf_text = extract_text_from_pdf(pdf_path)
    gemini_response = generate_response(prompt_template, pdf_text)

    try:
        # Gemini should return JSON-like content
        parsed_data = eval(gemini_response) if "{" in gemini_response else {"raw": gemini_response}
    except Exception:
        parsed_data = {"raw": gemini_response}

    return parsed_data
