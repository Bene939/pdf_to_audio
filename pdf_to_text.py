import pdfplumber
def pdf_to_text(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""  # Handle cases where text extraction might fail

    # Print or save the extracted text
    print(full_text)
    return full_text
