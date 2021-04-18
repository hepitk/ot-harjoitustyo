# Class that takes care of reading and writing to documents
import re
from docx import Document
from docx.shared import Pt

class DocumentHandler:
    def __init__(self, document):
        self.document = document
        self.to_be_replaced_list = []
        self.replace_list = []
    
    def add_to_be_replaced_list (self, word):
        self.to_be_replaced_list.append(word)

    def add_replace_list (self, word):
        self.replace_list.append(word)

    def replace_words(self, document):
        style = document.styles['Normal']
        font = style.font
        font.name = 'Calibri'
        font.size = Pt(12)
        for p in document.paragraphs:
            for i in range(0, len(self.to_be_replaced_list)):
                to_be_replaced = self.to_be_replaced_list[i]
                replace = self.replace_list[i]
                if to_be_replaced in p.text:
                    # print("found it!")
                    p.text = p.text.replace(to_be_replaced, replace)
        document.save("testi.docx")