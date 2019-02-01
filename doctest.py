# Reads the word document that you want to email
from docx import Document

# Just enter your word document file path. e.g C\Downloads\Pizza.docx
document = Document("Enter the word document file path")
docText = '\n'.join([
    paragraph.text.encode('utf-8') for paragraph in document.paragraphs
])
