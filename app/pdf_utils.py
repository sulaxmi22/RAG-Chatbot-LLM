# to read the pdf file
from pypdf import PdfReader

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    texts = ''
    for page in reader.pages:
        texts = texts + page.extract_text() or ''
    return texts