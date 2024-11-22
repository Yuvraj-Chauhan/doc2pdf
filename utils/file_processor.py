
import os
from docx import Document
from pathlib import Path

def save_uploaded_file(uploaded_file):
    file_path = Path(f"uploads/{uploaded_file.name}")
    file_path.parent.mkdir(exist_ok=True, parents=True)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def extract_metadata(file_path):
    doc = Document(file_path)
    word_count = sum(len(paragraph.text.split()) for paragraph in doc.paragraphs)
    file_size = os.path.getsize(file_path)
    return {
        "File Name": file_path.name,
        "Word Count": word_count,
        "File Size (KB)": round(file_size / 1024, 2),
    }
            