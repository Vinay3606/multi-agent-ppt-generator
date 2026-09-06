from pathlib import Path
from docx import Document
from pypdf import PdfReader


def read_docx(file_path):
    doc = Document(file_path)

    paragraphs = []

    for para in doc.paragraphs:
        text = para.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)


def read_pdf(file_path):
    reader = PdfReader(file_path)

    pages_text = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages_text.append(text)

    return "\n".join(pages_text)


def document_agent(file_path):
    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    if extension == ".docx":
        text = read_docx(file_path)

    elif extension == ".pdf":
        text = read_pdf(file_path)

    else:
        return {
            "status": "error",
            "message": "Unsupported document format"
        }

    word_count = len(text.split())

    return {
        "status": "success",
        "file_name": file_path.name,
        "file_type": extension,
        "word_count": word_count,
        "content": text
    }