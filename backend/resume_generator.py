import os
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIR = "backend/templates"
OUTPUT_DIR = "backend/uploads"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


def generate_resume_pdf(data: dict) -> str:
    template = env.get_template("resume_template.html")
    html_out = template.render(data=data)

    output_path = os.path.join(OUTPUT_DIR, f"{data['name'].replace(' ', '_')}_resume.pdf")
    HTML(string=html_out).write_pdf(output_path)
    print("Received data:", data)

    return output_path
