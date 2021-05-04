import unittest
from services.program_service import program_service


class TestProgramService(unittest.TestCase):
    def setUp(self):
        self._filename = "viranhaltijapäätös_määräalan_myynti_pohja"
        self._filename2 = "Testipohja"
        self._user_input_data = "Kiinteistötunnus"
        self._user_input_data2 = "Ostaja"
        self._placeholder = "[kiinteistötunnus]"
        self._placeholder2 = "[ostaja]"

    def test_create_replace_data_works(self):
        replace_data = program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        self.assertEqual(self._filename, replace_data.filename)
        self.assertEqual(self._user_input_data, replace_data.user_input_data)
        self.assertEqual(self._placeholder, replace_data.placeholder)

    def test_find_document_entries_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        program_service.create_replace_data(
            self._filename2, self._user_input_data2, self._placeholder2)
        document_names = program_service.find_all_document_names()
        self.assertEqual(self._filename, document_names[0])
        self.assertEqual(self._filename2, document_names[1])

    def test_document_exists_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        true = program_service.document_exists(self._filename2)
        false = program_service.document_exists("kana")
        self.assertEqual(true, True)
        self.assertEqual(false, False)
    
    def test_placeholder_duplicate_exists_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        true = program_service.placeholder_duplicate_exists(self._filename, self._placeholder)
        false = program_service.placeholder_duplicate_exists("Nikko", self._placeholder)
        false2 = program_service.placeholder_duplicate_exists(self._filename, "Auto")
        false3 = program_service.placeholder_duplicate_exists("Nikko", "Auto")
        self.assertEqual(true, True)
        self.assertEqual(false, False)
        self.assertEqual(false2, False)
        self.assertEqual(false3, False)