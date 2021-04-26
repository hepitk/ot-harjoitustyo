# Holds main program logic.
# Now hard-coded for testing purposes. TODO: Complete rework of ProgramService and UI
from docx import Document
from entities.replace_data import ReplaceData
from repositories.database_handler import database_handler
from services.document_handler import document_handler
from ui.ui import ui


class ProgramService:
    def start(self):
        replacing_words_list = []

        filename = "asiakirjapohjat/viranhaltijapäätös_määräalan_myynti_pohja"
        document = Document(filename + ".docx")
        user_input_data = "Syötä kiinteistötunnus:"
        placeholder = "[kiinteistötunnus]"
        replacing_words_list.append(ui.ask_question(user_input_data))
        instruction = ""
        replace_data = ReplaceData(
            filename, user_input_data, placeholder, instruction)
        database_handler.create(replace_data)

        user_input_data = "Syötä ostaja:"
        placeholder = "[ostaja]"
        replacing_words_list.append(ui.ask_question(user_input_data))
        instruction = ""
        replace_data = ReplaceData(
            filename, user_input_data, placeholder, instruction)
        database_handler.create(replace_data)

        document_entries = database_handler.find_document_entries(filename)

        calculator = 0
        for replace_data in document_entries:
            print("\n" + "Paikkamerkintä " + document_entries[calculator].placeholder + " korvattu" +
                  " sanalla " + replacing_words_list[calculator] + " " + "(" + str(document_handler.
                  replace_words(document, replace_data, replacing_words_list[calculator])) + " kpl)")
            calculator += 1

        ui.create_document(document_entries)


program_service = ProgramService()
