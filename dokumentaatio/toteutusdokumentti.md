# Toteutusdokumentti

## Ohjelman yleisrakenne

- `Ohjelma`: Ohjelman käyttöliittymä. Tulostaa ohjeet ja ohjaa funktiokutsut eteenpäin käyttäjän valintojen mukaan.
- `Levenshtein`: Varsinaisen laskennan suorittava luokka. Laskee editointietäisyydet, etsii sanakirjasta sopivia korjausvaihtoehtoja ja palauttaa ne käyttäjälle.
- `LevenshteinService`: Käsittelee `Levenshtein`-luokalle suunnatut kutsut. Muokkaa (mahdollisesti) käyttäjän antamia syötteitä ennen eteenpäin lähettämistä.
- `TrieSolmu`: Sanakirjan käyttämä Trie-tietorakenne.

## Saavutetut aika- ja tilavaativuudet
- Ei vielä selvillä

## Puutteet ja parannusehdotukset
- Sanasto on tällä hetkellä [wiktionarysta](https://en.lexipedia.org/), joka ikävä kyllä sisältää myös yleisiä kirjoitusvirheitä. Tämä ymmärrettävästi sotii ohjelman tarkoitusta vastaan. Sanasto on valittu koska se sisältää myös sanojen frekvenssit. Ilman frekvenssejä ohjelma saattaisi ehdottaa harvinaisia tai muuten outoja sanoja.
