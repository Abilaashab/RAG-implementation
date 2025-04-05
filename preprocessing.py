from PyPDF2 import PdfReader
import re

def read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    text= ""
    for page in reader.pages:
        text +=page.extract_text()
    return text

def preprocess_text(text:str) -> str:
    text = re.sub(r"\s+"," ", text) # Replace multiple spaces with single space
    text = text.strip().lower()
    return text

if __name__ == "__main__":
    pdf_file = "/Users/abilaasha/Documents/GitHub/Abi Github/RAG implementation/data/Clinical Query Agent FAQ.pdf"
    text = read_pdf(pdf_file)

    pre_process = preprocess_text(text)
    print(pre_process)