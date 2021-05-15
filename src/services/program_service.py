from docx import Document
from entities.replace_data import ReplaceData
from repositories.database_handler import database_handler
from services.document_handler import document_handler


class ProgramService:
    """Sovelluslogiikasta vastaava luokka. Muut luokat käyttävät tätä luokkaa operaatioihin."""

    def create_replace_data(self, document_name, user_input_data, placeholder):
        """Luo uuden ReplaceData-olion, joka sisältää yhden täyttötiedon. Lisää tiedon tietokantaan.

        Args:
            document_name: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            user_input_data: Merkkijono, joka kuvaa korvattavan tiedon tyyppiä.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Luotu täyttötieto ReplaceData-olion muodossa.
        """
        replace_data = ReplaceData(
            document_name, user_input_data, placeholder)
        database_handler.create(replace_data)
        return replace_data

    def find_document_replace_data_entries(self, filename):
        """Etsii kaikki tietylle asiakirjapohjalle lisätyt täyttötiedot.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
        Returns:
            Asiakirjapohjalle lisätyt täyttötiedot listana ReplaceData-olioita
        """
        document_entries = database_handler.find_document_replace_data_entries(filename)
        return document_entries

    def find_all_document_names(self):
        """Etsii kaikki järjestelmään lisätyt asiakirjapohjat.

        Returns:
            Järjestelmään lisättyjen asiakirjapohjien nimet listana merkkijonoja.
        """
        document_names = database_handler.find_all_document_names()
        return document_names

    def document_exists(self, filename):
        """Tarkistaa, löytyykö tietty asiakirjapohja kansiosta.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
        Returns:
            Palauttaa True, jos asiakirja löytyy kansiosta; False, jos asiakirjaa ei löydy.
        """
        try:
            Document("asiakirjapohjat/" + filename + ".docx")
        except:
            return False
        return True

    def placeholder_duplicate_exists(self, filename, placeholder):
        """Tarkistaa, löytyykö tietty paikkatieto järjestelmästä.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa True, jos paikkatieto löytyy järjestelmästä; False, jos paikkatietoa ei löydy.
        """
        if database_handler.find_filename_placeholder_pair(filename, placeholder):
            return True
        return False

    def find_all_replace_data_entries(self):
        """Hakee kaikki järjestelmään lisätyt ReplaceData-oliot

        Returns:
            Palauttaa ReplaceData-oliot listana järjestettynä aakkosjärjestykseen asiakirjapohjan tiedostonimen mukaan.
        """
        return database_handler.find_all_replace_data_entries()

    def delete_replace_data(self, filename, placeholder):
        """Poistaa halutun ReplaceData-olion järjestelmästä.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa True, jos poisto onnistui; False, jos epäonnistui.
        """
        if database_handler.delete_replace_data(filename, placeholder):
            return True
        return False


program_service = ProgramService()
