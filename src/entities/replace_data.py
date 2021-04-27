# Class that represents single replace data entry
from docx import Document


class ReplaceData:
    def __init__(self, filename, user_input_data, placeholder, instruction):
        self.filename = filename
        self.user_input_data = user_input_data
        self.placeholder = placeholder
        self.instruction = instruction
