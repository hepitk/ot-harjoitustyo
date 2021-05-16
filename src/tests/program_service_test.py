import unittest
from services.program_service import program_service
from initialize_database import drop_tables, initialize_database
from database_connection import get_database_connection


class TestProgramService(unittest.TestCase):
    def setUp(self):
        drop_tables(get_database_connection())
        initialize_database()
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
        drop_tables(get_database_connection())

    def test_find_document_replace_data_entries_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        program_service.create_replace_data(
            self._filename, self._user_input_data2, self._placeholder2)
        replace_data_entries = program_service.find_document_replace_data_entries(self._filename)
        self.assertEqual(self._user_input_data, replace_data_entries[0].user_input_data)
        self.assertEqual(self._user_input_data2, replace_data_entries[1].user_input_data)
        self.assertEqual(self._placeholder, replace_data_entries[0].placeholder)
        self.assertEqual(self._placeholder2, replace_data_entries[1].placeholder)
        drop_tables(get_database_connection())

    def test_find_all_document_names_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        program_service.create_replace_data(
            self._filename2, self._user_input_data2, self._placeholder2)
        program_service.create_replace_data(
            self._filename, self._user_input_data2, self._placeholder2)
        document_names = program_service.find_all_document_names()
        self.assertEqual(self._filename, document_names[0])
        self.assertEqual(self._filename2, document_names[1])
        drop_tables(get_database_connection())

    def test_document_exists_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        self.assertEqual(program_service.document_exists(self._filename2), True)
        self.assertEqual(program_service.document_exists("kana"), False)
        drop_tables(get_database_connection())

    def test_placeholder_duplicate_exists_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        self.assertEqual(program_service.placeholder_duplicate_exists(
            self._filename, self._placeholder), True)
        self.assertEqual(
            program_service.placeholder_duplicate_exists("Nikko", self._placeholder), False)
        self.assertEqual(
            program_service.placeholder_duplicate_exists(self._filename, "Auto"), False)
        self.assertEqual(
            program_service.placeholder_duplicate_exists("Nikko", "Auto"), False)
        drop_tables(get_database_connection())

    def test_find_all_replace_data_entries_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        program_service.create_replace_data(
            self._filename2, self._user_input_data2, self._placeholder2)
        program_service.create_replace_data(
            self._filename, self._user_input_data2, self._placeholder2)
        replace_data_entries = program_service.find_all_replace_data_entries()
        self.assertEqual(self._filename2, replace_data_entries[0].filename)
        self.assertEqual(self._user_input_data2, replace_data_entries[0].user_input_data)
        self.assertEqual(self._placeholder2, replace_data_entries[0].placeholder)
        self.assertEqual(self._filename, replace_data_entries[1].filename)
        self.assertEqual(self._user_input_data, replace_data_entries[1].user_input_data)
        self.assertEqual(self._placeholder, replace_data_entries[1].placeholder)
        self.assertEqual(self._filename, replace_data_entries[2].filename)
        self.assertEqual(self._user_input_data2, replace_data_entries[2].user_input_data)
        self.assertEqual(self._placeholder2, replace_data_entries[2].placeholder)
        drop_tables(get_database_connection())

    def test_delete_replace_data_works(self):
        program_service.create_replace_data(
            self._filename, self._user_input_data, self._placeholder)
        program_service.create_replace_data(
            self._filename2, self._user_input_data2, self._placeholder2)
        program_service.create_replace_data(
            self._filename, self._user_input_data2, self._placeholder2)
        program_service.delete_replace_data(self._filename2, self._placeholder2)
        replace_data_entries = program_service.find_all_replace_data_entries()
        self.assertEqual(self._filename, replace_data_entries[0].filename)
        self.assertEqual(self._filename, replace_data_entries[1].filename)
        drop_tables(get_database_connection())
