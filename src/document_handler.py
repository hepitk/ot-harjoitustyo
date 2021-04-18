# Class that takes care of reading and writing to documents
from docx import Document
from docx.shared import Pt
from replace_data import ReplaceData

class DocumentHandler:
    def replace_words(self, document, replace_data, replace_word):
        document = document
        placeholder = replace_data.placeholder

        style = document.styles["Normal"]
        font = style.font
        font.name = "Calibri"
        font.size = Pt(12)

        for p in document.paragraphs:            
            if placeholder in p.text:
                # print("found it!")
                p.text = p.text.replace(placeholder, replace_word)
        document.save("testi.docx")

document_handler = DocumentHandler()