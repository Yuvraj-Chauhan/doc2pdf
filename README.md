# DOCX to PDF Converter

A simple web application for converting DOCX files to PDF format. This project is built using Python and Streamlit, allowing users to upload DOCX files and convert them to high-quality PDFs. Additional features include the ability to add password protection to the converted PDFs.

## Features

- **DOCX to PDF Conversion**: Convert DOCX files to PDF format while preserving text and basic formatting.
- **Password Protection**: Add password protection to the converted PDFs.
- **File Metadata**: Extract basic metadata from DOCX files (e.g., file size, word count).
- **Interactive UI**: A simple and intuitive interface built using Streamlit.

## Technologies Used

- **Streamlit**: A Python library for building interactive web applications.
- **Aspose.Words**: A commercial library that provides high-fidelity DOCX to PDF conversion.
- **FPDF**: A Python library used for generating PDFs from DOCX files.
- **python-docx**: A Python library for working with DOCX files.

## Installation

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/docx-to-pdf-converter.git
cd docx-to-pdf-converter
```

### 2. Set up a Virtual Environment

Create a virtual environment to manage dependencies:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Required Dependencies

Install the necessary Python libraries:

```bash
pip install -r requirements.txt
```

**requirements.txt** should include the following:

```
streamlit
fpdf
python-docx
pypandoc  # Optional for higher-quality conversion
aspose-words  # Optional for commercial conversion
pywin32  # Optional for Microsoft Word Automation on Windows
```

### 4. Run the Application

To start the Streamlit application, use the following command:

```bash
streamlit run app.py
```

This will launch the web application in your browser where you can upload DOCX files and convert them to PDFs.

## How to Use

1. **Upload DOCX File**: Click the "Upload" button to select a DOCX file from your system.
2. **Convert to PDF**: After the file is uploaded, click the "Convert to PDF" button to start the conversion.
3. **Add Password Protection** (Optional): You can optionally add password protection to the converted PDF by entering a password in the provided field.
4. **Download PDF**: Once the conversion is complete, the PDF will be available for download.

## Optional Configurations

- **High-Quality Conversion**: For better formatting retention, you can enable `Aspose.Words` for high-quality conversion. These can be used for better handling of complex DOCX formatting.

## Example Use Case

- **Upload a DOCX file** with formatted text, headings, and images.
- **Click "Convert to PDF"** to convert it into a PDF.
- **Optional**: Add password protection to the PDF.
- **Download** the PDF and share it or save it for future reference.

## Acknowledgments

- **Streamlit**: For providing a simple and powerful framework for building web applications.
- **Aspose.Words**: For commercial-grade DOCX to PDF conversion.
- **FPDF**: For generating PDFs from DOCX files.
- **python-docx**: For reading DOCX files and extracting content.

## Troubleshooting

- **Poor Conversion Quality**: If the generated PDF is of poor quality or formatting is lost, try using the `Aspose.Words` library for better conversion quality.
- **Missing Libraries**: Ensure that all required libraries are installed. Use the `pip install -r requirements.txt` command to install them.

---

Feel free to modify and extend the application to fit your needs. Happy coding!

---

### Notes for Deployment

- **Streamlit Cloud**: This app can also be deployed on [Streamlit Cloud](https://streamlit.io/cloud). Ensure that the `requirements.txt` file is up to date for easy deployment.
- **Heroku/Other Platforms**: This app can be deployed to other cloud platforms by setting up the necessary environment and requirements.

## Future Enhancements

- **Image Support**: Add support for handling images in DOCX files during conversion.
- **Customization**: Allow users to choose the PDF output quality or other formatting options.

---

### Key Sections:

1. **Project Overview**: Provides an introduction to the app, what it does, and its features.
2. **Installation Instructions**: Guides users through setting up the project on their local machine or server.
3. **Usage**: Explains how to use the app through the web interface.
4. **Optional Configurations**: Details on optional settings like using higher-quality libraries or automation options.
