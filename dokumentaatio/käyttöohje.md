# TÄTI – Käyttöohje


## Ohjelman käynnistäminen

Asenna tarvittavat riippuvuudet poetryn kautta komennolla:

*poetry install*

Suorita sovellus komennolla:

*poetry run invoke start*

Windows-ympäristössä käytä komentoa:

*poetry run invoke start-windows*


## Asiakirjapohjat

1. Ennen sovelluksen käyttöä muokkaa asiakirjapohja haluamaksesi. Automatisoitua täyttöä tarvitsevaan kohtaan laita paikkatietomerkintä. Jos esimerkiksi haluat kiinteistötunnuksen 92-17-558-8 täytettynä useaan kohtaan asiakirjassa, voit käyttää paikkatietomerkintänä [kiinteistötunnus] -merkintää niissä kohdissa, joihin haluat tiedon täydentyvän. Paikkatietomerkintä voit käyttää mitä merkintää haluat, mutta suosittelen käyttämään hakasulkuja merkissä, jotta paikkatietomerkintä ei sekoitu muihin sanoihin.

2. Tallenna asiakirjapohja .docx-muodossa ohjelman juureen kansioon "asiakirjapohjat". HUOM! Vain .docx-muotoiset asiakirjat toimivat.

Ohjelmassa käytettävän kirjaston heikkouksista johtuen tietyn kappaleen sisällä olevat muutokset poistuvat. Esim. jos yksi sana keskellä kappaletta on lihavoituna, poistuu lihavointi. Lisäksi tällä hetkellä ohjelmassa voi käyttää vain fonttia Calibri (size 12).


## Ohjelman käyttö

### Alkuvalikko

Alkuvalikosta pääset Lisää täyttötietoja -näkymään painamalla nappia "Lisää" ja asiakirjapohjien täyttämiseen valitsemalla asiakirjapohjan nimen valikosta ja painamalla nappia "Valitse asiakirjapohja". Sinun on lisättävä täyttötietoja sovelukseen ennen kuin pystyt täyttämään asiakirjapohjia.

### Lisää täyttötietoja -näkymä

Tässä näkymässä voit lisätä täyttötietoja järjestelmään. Täyttötietojen pohjalta ohjelma täyttää halutut asiakirjapohjat.

1. Asiakirjapohjan nimeen täytä haluamasi asiakirjapohjan nimi ilman .docx-päätettä. HUOM! Nimen on oltava täsmälleen samassa muodossa kuin se on asiakirjapohjat-kansiossa.

2. Täytettävän tiedon tyyppiin täytä halutun tiedon tyyppi. Esim. jos paikkatieto koskee kiinteistötunnusta, täytä kohtaan sana "Kiinteistötunnus".

3. Paikkatietomerkintään täytä paikkatietomerkintä siinä muodossa kuin se on lisättynä asiakirjapohjaan. Esimerkkinä edellä mainittu [kiinteistötunnus]. HUOM! Paikkatietomerkkinnän on oltava täsmälleen samassa muodossa kuin se löytyy asiakirjapohjasta.

4. Paina "Lisää tieto" -nappia, kun haluat lisätä täyttötiedon järjestelmään. 

Järjestelmään voi lisätä useita asiakirjapohjia ja niille useita täyttötietoja. Samalle asiakirjapohjalle ei luonnollisesti voi lisätä kahta samaa paikkatietomerkintää.

### Täytä asiakirjapohja-näkymä

Tässä näkymässä voit täyttää järjestelmään lisätyn asiakirjapohjan järjestelmään lisätyillä täyttötiedoilla.

1. Täytä kaikki asiakirjapohjaa koskevat kohdat. Esimerkiksi edellä mainittuun kiinteistötunnusesimerkkiin syötä 92-17-558-8.

2. Paina "Täytä"-nappia ja ohjelma täyttää asiakirjapohjan paikkatietomerkinnällä varustetut kohdat syötetyllä tiedolla. Valmis asiakirja tallentuu "valmiit asiakirjat" -kansioon nimellä valmis.docx.


