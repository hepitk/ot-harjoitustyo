import re
from documenthandler import DocumentHandler
from docx import Document


def main():    
    real_estate_id = input("Syötä kiinteistötunnus:\n")
    print(f"Syötit kiinteistötunnuksen: {real_estate_id}")
       
    filename = "viranhaltijapäätös_määräalan_myynti_pohja.docx"
    document = Document(filename)

    document_handler = DocumentHandler(document)
    document_handler.add_to_be_replaced_list("[kiinteistötunnus]")
    document_handler.add_replace_list(real_estate_id)
    document_handler.replace_words(document_handler.document)

    print("Uusi asiakirja luotu")

if __name__ == "__main__":
    main()