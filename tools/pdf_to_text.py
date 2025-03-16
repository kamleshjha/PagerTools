from flask import request
import pdfplumber

def pdf_to_text_route():
    file = request.files["pdf"]
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text