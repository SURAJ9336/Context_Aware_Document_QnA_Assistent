import pdfplumber

def extract_text(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:  # check if not None
                text += page_text + "\n"
    return text.strip()
