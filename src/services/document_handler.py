# Class that takes care of reading and writing to documents
from docx.shared import Pt
from docx import Document


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
        font.size = Pt(11)
        section = document.sections[0]
        header = section.header
        footer = section.footer

        for par in document.paragraphs:
            if placeholder in par.text:
                replace_amount += 1
                par.text = par.text.replace(placeholder, user_input)
        for par in header.paragraphs:
            if placeholder in par.text:
                replace_amount += 1
                par.text = par.text.replace(placeholder, user_input)
        for par in footer.paragraphs:
            if placeholder in par.text:
                replace_amount += 1
                par.text = par.text.replace(placeholder, user_input)
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    for par in cell.paragraphs:
                        if placeholder in par.text:
                            replace_amount += 1
                            par.text = par.text.replace(placeholder, user_input)        

        document.save("valmiit asiakirjat/valmis.docx")
        return replace_amount


document_handler = DocumentHandler()
