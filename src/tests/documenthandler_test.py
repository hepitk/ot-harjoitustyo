import unittest
from documenthandler import DocumentHandler
from docx import Document

class TestDocumentHandler(unittest.TestCase):
    def setUp(self):
        filename = "viranhaltijapäätös_määräalan_myynti_pohja.docx"
        document = Document(filename)
        self.document_handler = DocumentHandler(document)
    
    def test_add_to_be_replaced_list_works(self):
        self.document_handler.add_to_be_replaced_list("kana")
        self.document_handler.add_to_be_replaced_list("muna")
        self.assertEqual(self.document_handler.to_be_replaced_list[0], "kana")
        self.assertEqual(self.document_handler.to_be_replaced_list[1], "muna")