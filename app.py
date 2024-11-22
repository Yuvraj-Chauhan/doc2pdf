import streamlit as st
from utils.file_processor import extract_metadata, save_uploaded_file
from utils.pdf_generator import convert_to_pdf, add_password_protection

# Set the page title and icon for the browser tab
st.set_page_config(
    page_title="DOCX to PDF Converter",  # Title of the page
    page_icon=":page_facing_up:",  # You can use an emoji or an icon path
    layout="centered"  # This centers the content
)

# Title
st.title("DOCX to PDF Converter")

# File Upload
uploaded_file = st.file_uploader("Upload a DOCX file", type="docx")

if uploaded_file:
    # Save uploaded file
    file_path = save_uploaded_file(uploaded_file)
    st.success(f"File uploaded successfully: {uploaded_file.name}")
    
    # Metadata Display
    metadata = extract_metadata(file_path)
    st.subheader("File Metadata")
    for key, value in metadata.items():
        st.write(f"**{key}:** {value}")
    
    # Convert to PDF
    pdf_path = None  # Initialize pdf_path to None
    
    if st.button("Convert to PDF"):
        try:
            pdf_path = convert_to_pdf(file_path)
            st.success("File converted successfully!")
            with open(pdf_path, "rb") as pdf_file:
                st.download_button(label="Download PDF", data=pdf_file, file_name="converted.pdf")
        except Exception as e:
            st.error(f"Error converting to PDF: {e}")

    # Add Password Protection (if pdf_path exists)
    if pdf_path and st.checkbox("Add Password Protection"):
        password = st.text_input("Enter Password", type="password")
        if st.button("Protect PDF"):
            try:
                protected_path = add_password_protection(pdf_path, password)
                st.success("Password protection added!")
                with open(protected_path, "rb") as protected_pdf:
                    st.download_button(label="Download Protected PDF", data=protected_pdf, file_name="protected.pdf")
            except Exception as e:
                st.error(f"Error adding password protection: {e}")
