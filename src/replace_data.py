# Class that represents single replace data entry
from docx import Document

class ReplaceData:
    def __init__(self, filename, user_question, placeholder, instruction):
        self.filename = filename
        self.document = Document(filename + ".docx")
        self.user_question = user_question
        self.placeholder = placeholder
        self.instruction = instruction