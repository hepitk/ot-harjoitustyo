# Viranhaltijapäätösten ja kiinteistön kauppakirjojen luontisovellus

Tämä sovellus luodaan työnantajani Vantaan kaupungin viranhaltijapäätösten ja kiinteistön kauppakirjojen laadintaa varten. 
Ongelmana organisaatiossa on, että samoja tietoja syötetään moneen kertaan monen eri henkilön toimesta viranhaltijapäätöspohjiin ja viranhaltijapäätösten pohjalta tehtäviin kiinteistön kauppakirjapohjiin.
Sovelluksen tarkoituksena on nopeuttaa Kaupunkiympäristön toimialan viranhaltijapäätöksien ja kiinteistön kauppakirjojen laadintaa.
Antamalla sovellukselle oikeat tiedot (mm. osapuolet, kiinteistötunnukset yms.), sovellus osaa luoda word-muotoisten täyttämättömien asiakirjapohjien perusteella word-muotoiset täytetyt asiakirjapohjat viranhaltijapäätöksistä ja kauppakirjoista. 
Sovellus siis säästää työntekijöiden aikaa ja vähentää virheitä tekemällä pohjien täyttämisestä nopeampaa ja vähentämällä turhaa työtä.

Toiminnallisuus:

- Sovelluksessa on graafinen käyttöliittymä, josta valitaan ensin, onko kaupunki kaupassa ostajana vai myyjänä
- Seuraavaksi sovellukseen annettaisiin kaupunginosa, sillä pohjat vaihtelevat hieman kaupunginosan mukaan
- Lopuksi käyttäjä antaa ainakin seuraavat tiedot (kaikkia tietoja ei tarvita jokaisessa kaupassa): myyjä ja ostaja (nimi, y-tunnus tai henkilötunnus, osoite, yhteyhenkilön nimi ja sähköposti), kiinteistötunnus ja kauppahinta (Lista täydentyy myöhemmin)

Tekninen toteutus:

- Tarkoitus on käyttää Pythonin python-docx-kirjastoa apuna (https://python-docx.readthedocs.io/en/latest/)
- Word-muotoiset pohjat löytyvät jo valmiiksi sovelluksen kansiosta, joten sovellus vain täyttäisi tarvittavat tiedot pohjien oikeisiin kohtiin ja tuloksena olisi täytetty pohja. Tyhjät pohjat saan Vantaan kaupungilta.

Laajentamismahdollisuudet:

- Sovellusta voi laajentaa niin, että se mahdollistaisi myös kiinteistövaihtojen, maanvuokrasopimukset ja muut sopimustyypit.
- Lopullisessa muodossaan sovelluksen voisi laajentaa myös asiakirjapohjien hallintajärjestelmäksi, mutta tämä ei ole tämän harjoitustyön laajuudessa mahdollista.
