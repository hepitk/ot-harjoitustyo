class ReplaceData:
    """Luokka, joka kuvastaa yhtä täyttötietoa yhdessä asiakirjapohjassa."""

    def __init__(self, filename, user_input_data, placeholder):
        self.filename = filename
        self.user_input_data = user_input_data
        self.placeholder = placeholder
