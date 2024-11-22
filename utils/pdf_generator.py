from pikepdf import Pdf
from docx2pdf import convert

import pythoncom
from docx2pdf import convert
from pathlib import Path

def convert_to_pdf(docx_path):
    pythoncom.CoInitialize()  # Initialize COM library
    try:
        # Ensure paths are properly handled
        output_pdf = Path(docx_path).with_suffix(".pdf")
        convert(docx_path, output_pdf)
        return output_pdf
    except Exception as e:
        raise RuntimeError(f"Error converting DOCX to PDF: {e}")

    
def add_password_protection(pdf_path, password):
    protected_path = pdf_path.with_name(f"{pdf_path.stem}_protected.pdf")
    with Pdf.open(pdf_path) as pdf:
        pdf.save(protected_path, encryption=Pdf.Encryption(owner=password, user=password))
    return protected_path