import re
from documenthandler import DocumentHandler
from docx import Document


def main():    
    real_estate_id = input("Syötä kiinteistötunnus:\n")
    print(f"Syötit kiinteistötunnuksen: {real_estate_id}")    
    
    document = Document("viranhaltijapäätös_määräalan_myynti_pohja.docx")
    document_handler = DocumentHandler()

    replaced = re.compile("kiinteistö_id")
    replace = real_estate_id
    document_handler.docx_replace_regex(document, replaced, replace)
    document.save("viranhaltijapäätös_määräalan_myynti.docx")

    print("Uusi asiakirja luotu")

if __name__ == "__main__":
    main()