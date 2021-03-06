# TÄTI – Täyttöbotti

Sovellus tarjoaa automaattisen .docx-muotoisten asiakirjapohjien täyttömahdollisuuden.
Asiakirjapohjia täytettäessä eri organisaatioissa ongelmana on, että samoja tietoja joutuu täyttämään useaan kertaan eri kohtiin erilaisissa asiakirjapohjissa.
Sovellus nopeuttaa asiakirjapohjien täyttäjien työtä: lisäämällä paikkatietomerkintöjä asiakirjapohjiin ja antamalla tarvittavat tiedot sovellukselle käyttäjä saa jatkossa täytettyä asiakirjapohjat nopeammin.
Esim. jos käyttäjä haluaa lisätä kiinteistötunnuksen useaan eri kohtaan tietyssä asiakirjapohjassa, lisää hän paikkatietomerkinnän (esim. [kiinteistötunnus]) haluamiinsa kohtiin asiakirjapohjassa ja sovellukselle tarvittavat tiedot annettuaan saa hän valmiin täytetyn asiakirjapohjan. 

## Release

[Release 1](https://github.com/hepitk/ot-harjoitustyo/releases/tag/viikko5)

[Release 2](https://github.com/hepitk/ot-harjoitustyo/releases/tag/viikko6)

[Final release](https://github.com/hepitk/ot-harjoitustyo/releases/tag/viikko7)


## Lähteet

Sovelluksen teossa on käytetty apuna materiaalia osoitteista https://ohjelmistotekniikka-hy.github.io/ ja https://github.com/ohjelmistotekniikka-hy/python-todo-app.


## Dokumentaatio

[Käyttöohje](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/käyttöohje.md)

[Määrittelydokumentti](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/maarittely.md)

[Tuntikirjanpito](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/hepitk/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)


## Asennus

### Sovelluksen asentaminen

Tarvittavat riippuvuudet asennetaan poetryn kautta komennolla:

*poetry install*


## Komennot

### Sovelluksen suorittaminen

Sovellus suoritetaan komennolla:

*poetry run invoke start*

Windows-ympäristössä käytetään komentoa:

*poetry run invoke start-windows*

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


## Sovelluksen tila ja puutteet

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

### Status 4.5.2021

Sovelluksen ulkoasua ja käytettävyyttä on paranneltu. Konsoliin tulostuu virheilmoituksia vääristä syötteistä. Käyttäjälle annettavista ohjeista luovuttu turhana, ne voi laittaa tietotyypin yhteyteen tarvittaessa.

Sovellukseen olisi vielä tehtävä näkymä, jossa näkee kaikki lisätyt täyttötiedot. Samassa näkymässä on oltava toiminnallisuus, joka mahdollistaa täyttötietojen poistamisen. Virheilmoitukset olisi konsolin asemesta saatava ponnahdusikkunaan. Täytä asiakirjapohja -ikkunaan olisi saatava scrollausmahdollisuus. Käyttöohjeeseen olisi hyvä saada kuvia.

### Loppupalautus 16.5.2021

Ohjelmaan on nyt toteutettu fontin muutosmahdollisuus, ja listtyjen täyttötietojen poistomahdollisuus. Virheilmoitukset näkyvät ilmoituksena, ikkunoita voi scrollata ja käyttöohjeeseen on lisätty kuvat.

Ohjelma täyttää sille asetetut vaatimukset melko hyvin. Koodin luettavuudessa ja testeissä olisi osin parannettavaa. 

Testeihin ei ole tehty testitietokantaa ja testaus tyhjentää tuotantotietokannan.

Ohjelmassa käytettävän kirjaston heikkouksista johtuen tietyn kappaleen sisällä olevat muutokset poistuvat. Koitin erilaisia menetelmiä tämän ongelman poistamiseen, mutta en onnistunut löytämään täysin toimivaa ratkaisua ongelmaan. Nykyinen implementaatio on yrityksistäni paras vaihtoehto. Nyt esimerkiksi jos yksi sana keskellä kappaletta on lihavoituna, poistuu lihavointi. Lisäksi asiakirjapohjia täytettäessä asiakirjapohjan fontti ja fonttikoko muuttuvat käyttämään ohjelman fonttia ja fonttikokoa.

Täytä asiakirjapohja -toiminnallisuus hyväksyy tyhjät kentät, mutta tämä on tarkoituksellista, sillä joskus jokin kenttä saatetaan haluta jättää tyhjäksi.
