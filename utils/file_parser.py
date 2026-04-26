from PyPDF2 import PdfReader
from docx import Document
import pdfplumber
import pytesseract
from PIL import Image
import io
import pandas as pd

SUPPORTED_TYPES = ["xlsx", "xls", "csv", "txt", "md", "pdf", "docx"]

def parse_file(file):
    text = ""
    file.seek(0)

    if file.name.endswith(".pdf"):
        # Try normal text extraction first
        reader = PdfReader(file)
        text = " ".join([page.extract_text() or "" for page in reader.pages])

        # If no text found, fallback to OCR
        if not text.strip():
            file.seek(0)
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    img = page.to_image(resolution=300).original
                    text += pytesseract.image_to_string(img)

    elif file.name.endswith(".docx"):
        doc = Document(io.BytesIO(file.read()))
        text = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

    elif file.name.endswith((".xlsx", ".xls")):
        df = pd.read_excel(file)
        text = df.to_string(index=False)

    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
        text = df.to_string(index=False)

    elif file.name.endswith((".txt", ".md")):
        text = file.read().decode("utf-8")

    # Normalize text
    text = text.lower()
    text = " ".join(text.split())
    return text
