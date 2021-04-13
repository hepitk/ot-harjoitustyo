import re
from documenthandler import DocumentHandler
from docx import Document


def main():    
    real_estate_id = input("Syötä kiinteistötunnus:\n")
    print(f"Syötit kiinteistötunnuksen: {real_estate_id}")    
    
    document = Document("viranhaltijapäätös_määräalan_myynti_pohja.docx")
    document_handler = DocumentHandler()

    to_be_replaced_list = ["[kiinteistötunnus]"]
    replace_list = [real_estate_id]
    document_handler.replace_words(document, to_be_replaced_list, replace_list)

    print("Uusi asiakirja luotu")

if __name__ == "__main__":
    main()