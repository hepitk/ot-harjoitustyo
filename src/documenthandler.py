# Class that takes care of replacing placeholders in the documents
import re
from docx import Document
from docx.shared import Pt

class DocumentHandler:
    def replace_words(self, document, to_be_replaced_list, replace_list):
        style = document.styles['Normal']
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(12)
        for p in document.paragraphs:            
            to_be_replaced = to_be_replaced_list[0]
            replace = replace_list[0]
            if to_be_replaced in p.text:
                # print("found it!")
                p.text = p.text.replace(to_be_replaced, replace)
        document.save("testi.docx")