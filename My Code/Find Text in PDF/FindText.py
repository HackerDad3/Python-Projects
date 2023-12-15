import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def find_and_save_matches(pdf_path, output_file):
    pdf_text = extract_text_from_pdf(pdf_path)
    pattern = r'\b[A-Za-z]{3}\.\d{4}\.\d{4}\.\d{4}\b'
    matches = re.findall(pattern, pdf_text)

    with open(output_file, 'w') as file:
        for match in matches:
            file.write(match + '\n')

# Example usage:
pdf_path = 'C:/Users/Willi/OneDrive/Documents/Python Projects/My Code/Find Text in PDF/20231215_affidavit.pdf'
output_file = 'C:/Users/Willi/OneDrive/Documents/Python Projects/My Code/Find Text in PDF/output.txt'
find_and_save_matches(pdf_path, output_file)
print(f'Script has completed. Text is saved to {output_file}')