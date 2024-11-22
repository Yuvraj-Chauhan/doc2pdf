from pikepdf import Pdf
from fpdf import FPDF
from docx import Document
from pathlib import Path

def convert_to_pdf(docx_path):
    pdf_path = Path(docx_path).with_suffix(".pdf")
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    try:
        # Load DOCX file
        doc = Document(docx_path)

        # Loop through paragraphs
        for paragraph in doc.paragraphs:
            # Encode text to handle special characters and decode them back to Unicode
            paragraph_text = paragraph.text.encode("latin-1", errors="replace").decode("latin-1")
            # Add paragraph text to PDF, wrapping long text
            pdf.multi_cell(0, 10, paragraph_text)

        # Output the PDF
        pdf.output(str(pdf_path))
        return pdf_path

    except Exception as e:
        raise RuntimeError(f"Error converting DOCX to PDF: {e}")
    
def add_password_protection(pdf_path, password):
    protected_path = pdf_path.with_name(f"{pdf_path.stem}_protected.pdf")
    with Pdf.open(pdf_path) as pdf:
        pdf.save(protected_path, encryption=Pdf.Encryption(owner=password, user=password))
    return protected_path
