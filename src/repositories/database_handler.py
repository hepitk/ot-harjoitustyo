from database_connection import get_database_connection
from entities.replace_data import ReplaceData


def get_replace_data_by_row(row):
    return ReplaceData(row["document_name"],
                       row["user_input_data"],
                       row["placeholder"],
                       ) if row else None

def get_all_document_names_by_row(row):
    return str(row["document_name"],) if row else None


class DatabaseHandler:
    """Tietokantaoperaatioista vastaava luokka."""

    def __init__(self, connection):
        self._connection = connection

    def create(self, replace_data):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into replace_data (document_name, user_input_data, placeholder)"
            "values (?, ?, ?)",
            (replace_data.filename, replace_data.user_input_data, replace_data.placeholder)
        )

        self._connection.commit()

        return replace_data

    def find_document_replace_data_entries(self, filename):
        cursor = self._connection.cursor()

        cursor.execute(
            "select document_name, user_input_data, placeholder from replace_data where document_name = ?",
            (filename,)
        )

        result = cursor.fetchall()

        return list(map(get_replace_data_by_row, result))

    def find_all_document_names(self):
        cursor = self._connection.cursor()

        cursor.execute(
            "select distinct document_name from replace_data"
        )

        result = cursor.fetchall()

        return list(map(get_all_document_names_by_row, result))

    def find_filename_placeholder_pair (self, filename, placeholder):
        cursor = self._connection.cursor()

        cursor.execute(
            "select document_name, placeholder from replace_data where document_name = ? AND placeholder = ?",
            (filename, placeholder,)
        )

        result = cursor.fetchone()

        if result is None:
            return False
        return True
    
    def find_all_replace_data_entries (self):
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from replace_data order by document_name"
        )

        result = cursor.fetchall()

        return list(map(get_replace_data_by_row, result))

    def delete_replace_data (self, filename, placeholder):
        cursor = self._connection.cursor()

        cursor.execute(
            "delete from replace_data where document_name = ? AND placeholder = ?",
            (filename, placeholder,)
        )

        cursor.execute(
            "select document_name, placeholder from replace_data where document_name = ? AND placeholder = ?",
            (filename, placeholder,)
        )

        result = cursor.fetchone()

        if result is None:
            return True
        return False


database_handler = DatabaseHandler(get_database_connection())
