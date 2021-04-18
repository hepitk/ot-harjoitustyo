import unittest
from document_handler import document_handler
from docx import Document
from replace_data import ReplaceData

class TestDocumentHandler(unittest.TestCase):
    def setUp(self):
        self.filename = "viranhaltijapäätös_määräalan_myynti_pohja"
        self.document = Document(self.filename + ".docx")
        self.document_filled = Document(self.document.save("testi.docx"))       
        self.user_question = "Syötä kiinteistötunnus:"
        self.placeholder = "[kiinteistötunnus]"
        self.replace_word = "kana"
        self.instruction = ""
        self.replace_data = ReplaceData(self.filename, self.user_question, self.placeholder, self.instruction)
    
    def test_replace_word_works(self):
        document_handler.replace_words(self.document, self.replace_data, self.replace_word)
        for p in self.document_filled.paragraphs:            
            if self.replace_word in p.text:
                replace_text = p.text.replace(self.placeholder, self.replace_word)
                self.assertEqual(replace_text, p.text)
