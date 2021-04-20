# Holds UI logic TODO: Complete rework
from docx import Document
from initialize_database import initialize_database
from entities.replace_data import ReplaceData
from repositories.database_handler import database_handler
from services.document_handler import document_handler


class UI:
    def ask_question(self, user_question):
        print("täällä")
        answer = input(user_question + "\n")
        print(f"Syötit kiinteistötunnuksen: {answer}")
        return answer

    def create_document(self, document_entries):
        print("\n" + "Uusi asiakirja luotu!")

        print("\n" + "Asiakirjapojalle lisätyt paikkamerkinnät:")
        for i in document_entries:
            print(i.placeholder)


ui = UI()
