from PyPDF2 import PdfReader
from docx import Document

def parse_file(file):

    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return " ".join([page.extract_text() or "" for page in reader.pages])

    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        return file.read().decode("utf-8", errors="ignore")