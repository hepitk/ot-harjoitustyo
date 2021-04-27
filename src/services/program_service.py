# Holds main program logic.
from entities.replace_data import ReplaceData
from repositories.database_handler import database_handler
from services.document_handler import document_handler


class ProgramService:

    def create_replace_data(self, document_name, user_input_data, placeholder, instruction):
        replace_data = ReplaceData(
            document_name, user_input_data, placeholder, instruction)
        database_handler.create(replace_data)
        return replace_data

    def find_document_entries(self, filename):
        document_entries = database_handler.find_document_entries(filename)
        return document_entries

    def find_all_document_names(self):
        document_names = database_handler.find_all_document_names()
        return document_names

    def replace_words(self, document, user_input, placeholder):
        document_handler.replace_words(document, user_input, placeholder)


program_service = ProgramService()
