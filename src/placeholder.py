# Class that represents single placeholder word in a document model, which will be replaced by user input
from docx import Document

class Placeholder(filename, user_question, placeholder, replace_word, instruction):
        self.document = Document(filename + ".docx")
        self.user_question = user_question
        self.placeholder = placeholder
        self.replace_word = replace_word
        self.instruction = instruction