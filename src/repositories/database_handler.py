from database_connection import get_database_connection
from entities.replace_data import ReplaceData


def get_replace_data_by_row(row):
    """Apufunktio, joka muuntaa tietokannasta haetut tiedot ReplaceData-olion muotoon.

    Args:
        row: Tietokannasta haettu rivi.
    Returns:
        ReplaceData-olio.
    """
    return ReplaceData(row["document_name"],
                       row["user_input_data"],
                       row["placeholder"],
                       ) if row else None

def get_all_document_names_by_row(row):
    """Apufunktio, joka muuntaa tietokannasta haetun asiakirjapohjan tiedostonimen merkkijonoksi.

    Args:
        row: Tietokannasta haettu rivi.
    Returns:
        Merkkijono, joka kuvaa asiakirjapohjan nimeä.
    """
    return str(row["document_name"],) if row else None


class DatabaseHandler:
    """Tietokantaoperaatioista vastaava luokka."""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection = sqlite3-tietokantayhteys.
        """
        self._connection = connection

    def create(self, replace_data):
        """Lisää luodun ReplaceData-olion tietokantaan

        Args:
            replace_data: ReplaceData-olio, joka kuvastaa yhtä täyttötietoa.
        Returns:
            Luotu täyttötieto ReplaceData-olion muodossa.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into replace_data (document_name, user_input_data, placeholder)"
            "values (?, ?, ?)",
            (replace_data.filename, replace_data.user_input_data, replace_data.placeholder)
        )

        self._connection.commit()

        return replace_data

    def find_document_replace_data_entries(self, filename):
        """Etsii kaikki tietylle asiakirjapohjalle lisätyt täyttötiedot tietokannasta.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
        Returns:
            Asiakirjapohjalle lisätyt täyttötiedot listana ReplaceData-olioita
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select document_name, user_input_data, placeholder from replace_data where document_name = ?",
            (filename,)
        )

        result = cursor.fetchall()

        return list(map(get_replace_data_by_row, result))

    def find_all_document_names(self):
        """Etsii kaikki tietokantaan lisätyt asiakirjapohjat.

        Returns:
            Tietokantaan lisättyjen asiakirjapohjien nimet listana merkkijonoja.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select distinct document_name from replace_data"
        )

        result = cursor.fetchall()

        return list(map(get_all_document_names_by_row, result))

    def find_filename_placeholder_pair (self, filename, placeholder):
        """Tarkistaa, löytyykö tietty paikkatieto tietokannasta.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa True, jos paikkatieto löytyy järjestelmästä; False, jos paikkatietoa ei löydy.
        """
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
        """Hakee kaikki tietokantaan lisätyt ReplaceData-oliot

        Returns:
            Palauttaa ReplaceData-oliot listana järjestettynä aakkosjärjestykseen asiakirjapohjan tiedostonimen mukaan.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select * from replace_data order by document_name"
        )

        result = cursor.fetchall()

        return list(map(get_replace_data_by_row, result))

    def delete_replace_data (self, filename, placeholder):
        """Poistaa halutun ReplaceData-olion järjestelmästä.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa True, jos ReplaceData-oliota ei poistooperaation jälkeen löydy tietokannasta; False, jos löytyy.
        """
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
