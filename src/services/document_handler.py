# Class that takes care of reading and writing to documents
from docx.shared import Pt


class DocumentHandler:

    def replace_words(self, document, user_input, placeholder):
        replace_amount = 0
        print(user_input)
        print(placeholder)

        style = document.styles["Normal"]
        font = style.font
        font.name = "Calibri"
        font.size = Pt(12)

        for par in document.paragraphs:
            if placeholder in par.text:
                replace_amount += 1
                par.text = par.text.replace(placeholder, user_input)
        document.save("valmiit asiakirjat/valmis.docx")
        return replace_amount


document_handler = DocumentHandler()
