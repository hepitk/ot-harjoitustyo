from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        DROP TABLE IF EXISTS Replace_data;
    """)

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE Replace_data (
            id INTEGER PRIMARY KEY,
            document_name TEXT,
            user_input_data TEXT,
            placeholder TEXT
        );
    """)

    connection.commit()

def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
