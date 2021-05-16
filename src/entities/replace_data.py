class ReplaceData:
    """Luokka, joka kuvaa yhtä täyttötietoa yhdessä asiakirjapohjassa."""

    def __init__(self, filename, user_input_data, placeholder):
        """Luokan konstruktori.

        Args:
            filename: Merkkijono, joka kuvaa asiakirjapohjan nimeä ilman .docx-päätettä.
            user_input_data: Merkkijono, joka kuvaa korvattavan paikkatietomerkinnän tietotyyppiä.
                Kertoo käyttäjälle mitä tietoa pitää syöttää.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        """
        self.filename = filename
        self.user_input_data = user_input_data
        self.placeholder = placeholder
