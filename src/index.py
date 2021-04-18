from docx import Document
from initialize_database import initialize_database
from replace_data import ReplaceData
from database_handler import database_handler
from document_handler import document_handler


def main():
    initialize_database()
    replace_words_list = []    

    filename = "viranhaltijapäätös_määräalan_myynti_pohja"
    document = Document(filename + ".docx")
    user_question = "Syötä kiinteistötunnus:"
    placeholder = "[kiinteistötunnus]"
    replace_words_list.append(input(user_question + "\n"))
    print(f"Syötit kiinteistötunnuksen: {replace_words_list[0]}")
    instruction = ""
    replace_data = ReplaceData(filename, user_question, placeholder, instruction)
    database_handler.create(replace_data)

    #filename = "viranhaltijapäätös_määräalan_myynti_pohja"
    user_question = "Syötä ostaja"
    placeholder = "[ostaja]"
    replace_words_list.append(input(user_question + "\n"))
    print(f"Syötit ostajan: {replace_words_list[1]}")
    instruction = ""
    replace_data = ReplaceData(filename, user_question, placeholder, instruction)
    database_handler.create(replace_data)

    document_entries = database_handler.find_document_entries(filename)
    
    calculator = 0
    for d in document_entries:        
        document_handler.replace_words(document, d, replace_words_list[calculator])
        calculator += 1
    print("\n" + "Uusi asiakirja luotu!")
    
    print("\n" + "Asiakirjan pohjaan lisätyt paikkatietomerkinnät:")
    for i in document_entries:
       print(i.placeholder)

if __name__ == "__main__":
    main()