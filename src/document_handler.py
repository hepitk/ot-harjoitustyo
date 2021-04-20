# Class that takes care of reading and writing to documents
from docx import Document
from docx.shared import Pt
from replace_data import ReplaceData


class DocumentHandler:
    def replace_words(self, document, replace_data, replace_word):
        placeholder = replace_data.placeholder
        replace_amount = 0

        style = document.styles["Normal"]
        font = style.font
        font.name = "Calibri"
        font.size = Pt(12)

        for par in document.paragraphs:
            if placeholder in par.text:
                replace_amount += 1
                par.text = par.text.replace(placeholder, replace_word)
        document.save("valmiit asiakirjat/testi.docx")
        return replace_amount


document_handler = DocumentHandler()
