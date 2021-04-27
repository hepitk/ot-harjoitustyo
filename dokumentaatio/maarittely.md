# Viranhaltijapäätösten ja kiinteistön kauppakirjojen luontisovellus

Tämä sovellus luodaan työnantajani Vantaan kaupungin viranhaltijapäätösten ja kiinteistön kauppakirjojen laadintaa varten. 
Ongelmana organisaatiossa on, että samoja tietoja syötetään moneen kertaan monen eri henkilön toimesta viranhaltijapäätöspohjiin ja viranhaltijapäätösten pohjalta tehtäviin kiinteistön kauppakirjapohjiin.
Sovelluksen tarkoituksena on nopeuttaa Kaupunkiympäristön toimialan viranhaltijapäätöksien ja kiinteistön kauppakirjojen laadintaa.
Antamalla sovellukselle oikeat tiedot (mm. osapuolet, kiinteistötunnukset yms.), sovellus osaa luoda word-muotoisten täyttämättömien asiakirjapohjien perusteella word-muotoiset täytetyt asiakirjapohjat viranhaltijapäätöksistä ja kauppakirjoista. 
Sovellus siis säästää työntekijöiden aikaa ja vähentää virheitä tekemällä pohjien täyttämisestä nopeampaa ja vähentämällä turhaa työtä.

Toiminnallisuus:

- TURHA Sovelluksessa on graafinen käyttöliittymä, josta valitaan ensin, onko kaupunki kaupassa ostajana vai myyjänä
- TURHA Seuraavaksi sovellukseen annettaisiin kaupunginosa, sillä pohjat vaihtelevat hieman kaupunginosan mukaan
- TEHTY Lopuksi käyttäjä antaa ainakin seuraavat tiedot (kaikkia tietoja ei tarvita jokaisessa kaupassa): myyjä ja ostaja (nimi, y-tunnus tai henkilötunnus, osoite, yhteyhenkilön nimi ja sähköposti), kiinteistötunnus ja kauppahinta (Lista täydentyy myöhemmin)
- TEHTY Käyttäjä voi lisätä omia tietoja, paikkamerkkejä ja pohjia järjestelmään

Tekninen toteutus:

- TEHTY Tarkoitus on käyttää Pythonin python-docx-kirjastoa apuna (https://python-docx.readthedocs.io/en/latest/)
- TEHTY/TURHA(KÄYTTÄJÄ LISÄÄ) Word-muotoiset pohjat löytyvät jo valmiiksi sovelluksen kansiosta, joten sovellus vain täyttäisi tarvittavat tiedot pohjien oikeisiin kohtiin määriteltynä paikkamerkkejä käyttäen ja tuloksena olisi täytetty pohja. Tyhjät pohjat saan Vantaan kaupungilta.
- TEHTY Tarvittavat tiedot tallennetaan tietokantaan. Näitä ovat käyttäjältä kysyttävä kysymys, paikkamerkki, mahdolliset täyttöohjeet ja asiakirjapohjan nimi.

Laajentamismahdollisuudet:

- Sovellusta voi laajentaa niin, että se mahdollistaisi myös kiinteistövaihtojen, maanvuokrasopimukset ja muut sopimustyypit.
- Lopullisessa muodossaan sovelluksen voisi laajentaa myös asiakirjapohjien hallintajärjestelmäksi, mutta tämä ei ole tämän harjoitustyön laajuudessa mahdollista.
