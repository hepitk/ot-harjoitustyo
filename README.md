# Viranhaltijapäätösten ja kiinteistön kauppakirjojen luontisovellus

Tämä sovellus luodaan työnantajani Vantaan kaupungin viranhaltijapäätösten ja kiinteistön kauppakirjojen laadintaa varten. 
Ongelmana organisaatiossa on, että samoja tietoja syötetään moneen kertaan monen eri henkilön toimesta viranhaltijapäätöspohjiin ja viranhaltijapäätösten pohjalta tehtäviin kiinteistön kauppakirjapohjiin.
Sovelluksen tarkoituksena on nopeuttaa Kaupunkiympäristön toimialan viranhaltijapäätöksien ja kiinteistön kauppakirjojen laadintaa.
Antamalla sovellukselle oikeat tiedot (mm. osapuolet, kiinteistötunnukset yms.), sovellus osaa luoda word-muotoisten täyttämättömien asiakirjapohjien perusteella word-muotoiset täytetyt asiakirjapohjat viranhaltijapäätöksistä ja kauppakirjoista. 
Sovellus siis säästää työntekijöiden aikaa ja vähentää virheitä tekemällä pohjien täyttämisestä nopeampaa ja vähentämällä turhaa työtä.


## Dokumentaatio

[Määrittelydokumentti](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/maarittely.md)

[Tuntikirjanpito](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Asennus

### Sovelluksen asentaminen

Asenna tarvittavat riippuvuude poetryn kautta komennolla:

*poetry install*

### Sovelluksen käynnistäminen

Käynnistä sovellus komennolla:

*poetry run invoke start*

## Komennot

### Sovelluksen suorittaminen

Sovellus suoritetaan komennolla:

*poetry run invoke start*

### Testaus

Sovlluksen testit suoritetaan komennolla:

*poetry run invoke test*

### Testikattavuus

Testikattavuusraportin saa komennolla:

*poetry run invoke coverage-report*

Raportti muodostetaan htmlcov-hakemistoon.


## Sovelluksen tila 

### Status 13.4.2021 ja seuraavat askeleet

Sovellukseen on nyt tehty toiminnallisuus kiinteistötunnuksen lisäämiseksi paikkatiedon "[kiinteistötunnus]" kohdalle viranhaltijapäätöspohjassa. Tältä pohjalta sovellusta on hyvä laajentaa.

Python-docx-kirjastossa ei löytynyt erillistä replace()-metodia, joten sellaisen joutui soveltamaan itse nettiä apuna käyttäen, ja tämä tuotti hankaluuksia.
Tällä hetkellä sovellus toimii, mutta se ei salli erilaisia tyylejä yhden kappaleen sisällä. Jos siis asiakirjapohjamallissa on saman kappaleen sisällä erilaisia fontteja tai muita muotoiluja, ne häviävät. Tähän en keksinyt toimivaa ratkaisua.

Seuraavaksi toteutan tietokantayhteyden.