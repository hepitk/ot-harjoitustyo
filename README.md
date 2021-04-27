# TÄTI – Täyttöbotti

Tämä sovellus luodaan työnantajani Vantaan kaupungin viranhaltijapäätösten ja kiinteistön kauppakirjojen laadintaa varten. 
Ongelmana organisaatiossa on, että samoja tietoja syötetään moneen kertaan monen eri henkilön toimesta viranhaltijapäätöspohjiin ja viranhaltijapäätösten pohjalta tehtäviin kiinteistön kauppakirjapohjiin.
Sovelluksen tarkoituksena on nopeuttaa Kaupunkiympäristön toimialan viranhaltijapäätöksien ja kiinteistön kauppakirjojen laadintaa.
Antamalla sovellukselle oikeat tiedot (mm. osapuolet, kiinteistötunnukset yms.), sovellus osaa luoda word-muotoisten täyttämättömien asiakirjapohjien perusteella word-muotoiset täytetyt asiakirjat mm. viranhaltijapäätöksistä ja kauppakirjoista. 
Sovellus siis säästää työntekijöiden aikaa ja vähentää virheitä tekemällä pohjien täyttämisestä nopeampaa ja vähentämällä turhaa työtä.

## Release

[Uusin release](https://github.com/hepitk/ot-harjoitustyo/releases/tag/viikko5)


## Lähteet

Sovelluksen teossa on käytetty apuna materiaalia osoitteista https://ohjelmistotekniikka-hy.github.io/ ja https://github.com/ohjelmistotekniikka-hy/python-todo-app.


## Dokumentaatio

[Määrittelydokumentti](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/maarittely.md)

[Tuntikirjanpito](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)


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

### Laatutarkistus

Koodin laatutarkistuksen saa komennolla:

*poetry run invoke lint*

### Formatointi

Koodin formatoinnin saa komennolla:

*poetry run invoke format*


## Sovelluksen tila 

### Status 13.4.2021

Sovellukseen on nyt tehty toiminnallisuus kiinteistötunnuksen lisäämiseksi paikkatiedon "[kiinteistötunnus]" kohdalle viranhaltijapäätöspohjassa. Tältä pohjalta sovellusta on hyvä laajentaa.

Python-docx-kirjastossa ei löytynyt erillistä replace()-metodia, joten sellaisen joutui soveltamaan itse nettiä apuna käyttäen, ja tämä tuotti hankaluuksia.
Tällä hetkellä sovellus toimii, mutta se ei salli erilaisia tyylejä yhden kappaleen sisällä. Jos siis asiakirjapohjamallissa on saman kappaleen sisällä erilaisia fontteja tai muita muotoiluja, ne häviävät. Tähän en keksinyt toimivaa ratkaisua.

Seuraavaksi toteutan tietokantayhteyden.

### Status 20.4.2021

Sovellukseen on tehty tietokantayhteys ja tietokantaoperaatioita. Perusrakennetta päivitetty. Pylint ja autopep otettu käyttöön.

Tällä hetkellä sovelluksessa on kuitenkin vain testikäyttöliittymä, joka sekin suurimmaksi osaksi kovakoodattu.

Seuraavaksi on toteutettava graafinen käyttöliittymä ja kunnollinen sovelluslogiikka.

### Status 27.4.2021

Sovelluksessa on nyt alustava käyttöliittymä ja uusi sovelluslogiikka. Käyttäjä voi lisätä asiakirjapohjia hakemistoon "asiakirjapohjat". Alkunäkymässä käyttäjä voi valita täyttötietojen lisäämisen tai asiakirjapohjan täyttämisen. Täyttötietojen lisäämisessä asiakirjan nimi on annettava ilman .docx-päätettä ja täsmällisessä muodossa. Kun käyttäjä on lisännyt täyttötietoja, voi asiakirjapohjat täyttää niiden perusteella omassa näkymässään. Lopullinen asiakirja generoituu hakemistoon "valmiit asiakirjat" nimellä 
valmis.docx. 

Tällä hetkellä sovellus täyttää määrittelydokumentin vaatimukset. Sovelluksen kehityksen aikana on ilmennyt, että osa määrittelydokumentin vaatimuksista on turhia.

Sovelluksen ulkoasussa, käyttöliittymässä, koodissa ja toiminnallisuuksissa on vielä paljon parannettavaa. Käyttäjälle annettavat ohjeet eivät vielä näy missään.