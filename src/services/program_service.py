from entities.replace_data import ReplaceData
from repositories.database_handler import database_handler
from services.document_handler import document_handler


class ProgramService:
    """Sovelluslogiikasta vastaava luokka."""

    def create_replace_data(self, document_name, user_input_data, placeholder):
        """Luo uuden ReplaceData-olion, joka sisältää yhden täyttötiedon.

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

    def find_document_entries(self, filename):
        """Etsii kaikki tietylle asiakirjapohjalle lisätyt täyttötiedot.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
        Returns:
            Asiakirjalle lisätyt täyttötiedot listana ReplaceData-olioita
        """

        document_entries = database_handler.find_document_entries(filename)
        return document_entries

    def find_all_document_names(self):
        """Etsii kaikki järjestelmään lisätyt asiakirjapohjat.

        Returns:
            Järjestelmään lisättyjen asiakirjapohjien nimet listana merkkijonoja.
        """

        document_names = database_handler.find_all_document_names()
        return document_names

    def replace_words(self, document, user_input, placeholder):
        """Korvaa paikkatiedon halutulla käyttäjän syötteellä DocumentHandler-luokkaa hyväksi käyttäen, ja luo valmiin asiakirjan /valmiit asiakirjat -kansioon.

        Args:
            document: Muokattava asiakirjapohja docx-kirjaston Document-muodossa 
            user_input: Merkkijono, joka kuvaa käyttäjän syötettä ja jolla halutaan korvata paikkatietomerkintä asiakirjapohjassa.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa korvattujen sanojen lukumäärän.
        """

        return (document_handler.replace_words(document, user_input, placeholder))

    def document_exists(self, filename):
        """Tarkistaa, löytyykö tietty asiakirjapohja järjestelmästä.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
        Returns:
            Palauttaa True, jos asiakirja löytyy järjestelmästä; False, jos asiakirjaa ei löydy.
        """

        if database_handler.document_exists(filename):
            return True
        return False

    def placeholder_duplicate_exists(self, filename, placeholder):
        """Tarkistaa, löytyykö tietty paikkatieto järjestelmästä.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            user_input_data: Merkkijono, joka kuvaa korvattavan tiedon tyyppiä. (Tässä turha, mutta on mukana ReplaceData-oliossa ja tietokantaoperaatiossa)
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa True, jos paikkatieto löytyy järjestelmästä; False, jos paikkatietoa ei löydy.
        """
        
        if database_handler.find_filename_placeholder_pair(filename, placeholder):
            return True
        return False


program_service = ProgramService()
