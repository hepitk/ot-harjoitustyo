# Class that takes care of database operations
from database_connection import get_database_connection
from placeholder import Placeholder


database_handler = DatabaseHandler(get_database_connection())

class DatabaseHandler:
    def __init__(self, connection):
        self._connection = connection

    def create(self, placeholder):
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into placeholders (document_name, user_question, placeholder, replace_word, instruction) values (?, ?, ?, ?, ?)',
            (placeholder.document, placeholder.user_question, placeholder.placeholder, placeholder.replace_word, placeholder.insruction)
        )

        self._connection.commit()

        return placeholder