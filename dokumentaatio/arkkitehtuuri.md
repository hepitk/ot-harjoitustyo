# Arkkitehtuuri

## Luokkakaavio

![Luokkakaavio](./kuvat/luokkakaavio.png)

UI-luokka huolehtii käyttöliittymän logiikasta ja ProgramService suurimmasta osasta sovelluslogiikkaa.

ReplaceData-olioon tallennetaan sanojen korvauksessa tarvittavat tiedot. Näitä ovat asiakirjapohjan nimi, mitä tietoa käyttäjältä halutaan syöttävän, paikkamerkki ja mahdollinen täyttöohje käyttäjälle(esim. missä sijamuodossa tieto halutaan).

DocumentHandler-luokka huolehtii korvaavan sanan kirjoittamisesta .docx-muotoisesta asiakirjapohjasta löytyvän paikkatiedon paikalle sekä asiakirjan lukemisesta ja tallentamisesta.
Asiakirjapohjat löytyvät ohjelman juuresta kansiosta "asiakirjapohjat", ja valmiit asiakirjat tallennetaan "valmiit asiakirjat"-kansioon.

DatabaseHandler-luokka vastaa tiedon pysyväistalennetamisesta tietokantaan ja tietokannasta hakemisesta. ProgramService-luokka välittää ReplaceData-olion tiedot luokalle.

