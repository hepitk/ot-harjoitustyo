# Class that takes care of database operations
from database_connection import get_database_connection
from replace_data import ReplaceData


def get_replace_data_by_row(row):
    return ReplaceData(row["document_name"], row["user_question"], row["placeholder"], row["instruction"],) if row else None


class DatabaseHandler:
    def __init__(self, connection):
        self._connection = connection

    def create(self, replace_data):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into replace_data (document_name, user_question, placeholder, instruction) values (?, ?, ?, ?)",
            (replace_data.filename, replace_data.user_question,
             replace_data.placeholder, replace_data.instruction)
        )

        self._connection.commit()

        return replace_data

    def find_document_entries(self, filename):
        cursor = self._connection.cursor()

        cursor.execute(
            "select document_name, user_question, placeholder, instruction from replace_data where document_name = ?",
            (filename,)
        )

        result = cursor.fetchall()

        return list(map(get_replace_data_by_row, result))


database_handler = DatabaseHandler(get_database_connection())
