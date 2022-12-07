# Toteutusdokumentti

## Ohjelman yleisrakenne

- `Ohjelma`: Ohjelman käyttöliittymä. Tulostaa ohjeet ja ohjaa funktiokutsut eteenpäin käyttäjän valintojen mukaan.
- `Levenshtein`: Varsinaisen laskennan suorittava luokka. Laskee editointietäisyydet, etsii sanakirjasta sopivia korjausvaihtoehtoja ja palauttaa ne käyttäjälle.
- `LevenshteinService`: Käsittelee `Levenshtein`-luokalle suunnatut kutsut. Muokkaa (mahdollisesti) käyttäjän antamia syötteitä ennen eteenpäin lähettämistä.
- `TrieSolmu`: Sanakirjan käyttämä Trie-tietorakenne.

## Ohjelman toiminta (Kesken)

Ohjelma toimii pääpiirteittäin seuraavasti:

Käyttäjä syöttää ohjelmalle lauseen. Ohjelma tarkistaa jokaisen sanan kohdalla, löytyykö se sanakirjasta. Jos sana löytyy, lisätään se lopulliseen korjattuun lauseeseen sellaisenaan. Jos sanaa ei ole sanakirjassa, ohjelma kutsuu `levenshtein`-luokan `etsi`-metodia, joka palauttaa listan mahdollisista korjausvaihtoehdoista. Korjausvaihtoehtojen valinta perustuu niin sanottuun editointietäisyyteen, joka ilmaisee kuinka monta eri operaatiota sanalle on tehtävä, että siitä saadaan jokin eri sana.

Käytössä on neljä eri operaatiota:
- poisto: morn**n**ing ==> morning
- lisäys: mornin ==> mornin**g**
- vaihto: mor**m**ing ==> mor**n**ing
- siirto: **om**rning ==> **mo**rning

Jokaisen operaation "kustannus" on yksi (1). Mitä pienempi kustannus, sitä suuremmalla todennäköisyydellä se on haluamamme sana.

Etäisyydet lasketaan muodostamalla kaksiulotteinen taulukko:

|   |   | s | a | t | u | r | d | a | y |
| - | - | - | - | - | - | - | - | - | - |
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| s | 1 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| u | 2 | 1 | 1 | 2 | 2 | 3 | 4 | 5 | 6 |
| n | 3 | 2 | 2 | 2 | 3 | 3 | 4 | 5 | 6 |
| d | 4 | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 5 |
| a | 5 | 4 | 3 | 4 | 4 | 4 | 4 | 3 | 4 |
| y | 6 | 5 | 4 | 4 | 5 | 5 | 5 | 4 | 3 |

(Esimerkki [Wikipediasta](https://en.wikipedia.org/wiki/Levenshtein_distance))

Jatkuu...

## Saavutetut aika- ja tilavaativuudet
- Ei vielä selvillä

## Puutteet ja parannusehdotukset
- Sanasto on tällä hetkellä [wiktionarysta](https://en.lexipedia.org/), joka ikävä kyllä sisältää myös yleisiä kirjoitusvirheitä. Tämä ymmärrettävästi sotii ohjelman tarkoitusta vastaan. Sanasto on valittu koska se sisältää myös sanojen frekvenssit. Ilman frekvenssejä ohjelma saattaisi ehdottaa harvinaisia tai muuten outoja sanoja.
