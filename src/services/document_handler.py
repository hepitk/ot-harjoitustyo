# Class that takes care of reading and writing to documents
from docx.shared import Pt


class DocumentHandler:
    """Luokka, joka vastaa asiakirjapohjien muokkaamisesta ja valmiiden asiakirjojen luomisesta."""

    def replace_words(self, document, user_input, placeholder):
        """Korvaa paikkatiedon halutulla käyttäjän syötteellä, ja luo valmiin asiakirjan.

        Args:
            document: Muokattava asiakirjapohja docx-kirjaston Document-muodossa
            user_input: Merkkijono, joka kuvaa käyttäjän syötettä ja jolla halutaan korvata paikkatietomerkintä asiakirjapohjassa.
            placeholder: Merkkijono, joka kuvaa paikkatietomerkintää asiakirjapohjassa.
        Returns:
            Palauttaa korvattujen sanojen lukumäärän.
        """

        replace_amount = 0

        style = document.styles["Normal"]
        font = style.font
        font.name = "Calibri"
        font.size = Pt(12)

        for par in document.paragraphs:
            if placeholder in par.text:
                replace_amount += 1
                par.text = par.text.replace(placeholder, user_input)
        document.save("valmiit asiakirjat/valmis.docx")
        return replace_amount


document_handler = DocumentHandler()
