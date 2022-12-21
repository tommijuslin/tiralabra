# Toteutusdokumentti

## Ohjelman yleisrakenne

- `Ohjelma`: Ohjelman käyttöliittymä. Tulostaa ohjeet ja ohjaa funktiokutsut eteenpäin käyttäjän valintojen mukaan.
- `Levenshtein`: Varsinaisen laskennan suorittava luokka. Laskee editointietäisyydet, etsii sanakirjasta sopivia korjausvaihtoehtoja ja palauttaa ne.
- `Lauseenkorjaaja`: Muodostaa lopullisen korjatun lauseen käyttäjän valintojen perusteella.
- `TrieSolmu`: Sanakirjan käyttämä Trie-tietorakenne.

## Ohjelman toiminta

Käyttäjän syöttämä lause annetaan `Lauseenkorjaaja`-luokalle, joka tarkistaa jokaisen sanan kohdalla, löytyykö se sanakirjasta. Jos sana löytyy, lisätään se lopulliseen korjattuun lauseeseen sellaisenaan. Jos sanaa ei ole sanakirjassa, ohjelma kutsuu `Levenshtein`-luokan `etsi`-metodia, joka palauttaa listan mahdollisista korjausvaihtoehdoista.

### Editointietäisyys

Korjausvaihtoehtojen valinta perustuu niin sanottuun editointietäisyyteen, joka ilmaisee kuinka monta eri operaatiota sanalle on tehtävä, että siitä saadaan jokin eri sana.

Käytössä on neljä eri operaatiota:
- poisto: morn**n**ing ==> morning
- lisäys: mornin ==> mornin**g**
- vaihto: mor**m**ing ==> mor**n**ing
- siirto: **om**rning ==> **mo**rning

Jokaisen operaation "kustannus" on yksi (1). Mitä pienempi kustannus, sitä suuremmalla todennäköisyydellä se on haluamamme sana.

`Levenshtein`-luokka laskee etäisyydet muodostamalla kaksiulotteisen taulukon:

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

Taulukon viimeinen luku ilmaisee lopullisen editointietäisyyden. Listalle lisätään kaikki sanakirjasta löytyvät sanat, joiden etäisyys annettuun sanaan ei ylitä koodiin määriteltyä maksimietäisyyttä.

### Trie-tietorakenne

Sanasto on talletettu puumaiseen trie-tietorakenteeseen, missä jokainen puun solmu vastaa yhtä kirjainta.

<br>

<img src="https://github.com/tommijuslin/tiralabra/blob/main/dokumentaatio/trie.png" width=50% height=50%>

<br>

Trie-tietorakenne tekee vertailusta tehokkaampaa, sillä esimerkiksi sanat *bat* ja *bats* eroavat toisistaan vain viimeisen kirjaimen kohdalla, jolloin sanan *bats* kohdalla suurin osa laskennasta on tehty jo valmiiksi.

### Lopullinen korjattu lause

`Levenshtein`-luokan palauttamat korjausvaihtoehdot järjestetään ensin sanojen frekvenssien mukaan ja sitten editointietäisyyksien mukaan. Mitä yleisempi sana on ja mitä pienempi sen etäisyys väärinkirjoitetusta sanasta on, sitä todennäköisemmin se on käyttäjän haluama sana.

Käyttäjälle näytetään jokaiselle väärinkirjoitetulle sanalle lista mahdollisista korjausvaihtoehdoista, joista käyttäjä voi valita halumansa sanan. Valitut sanat lisätään lopulliseen lauseeseen ja kaikkien valintojen jälkeen korjattu lause näytetään käyttäjälle.


## Puutteet ja parannusehdotukset
- Sanasto on tällä hetkellä [wiktionarysta](https://en.lexipedia.org/), joka ikävä kyllä sisältää myös yleisiä kirjoitusvirheitä. Tämä ymmärrettävästi sotii ohjelman tarkoitusta vastaan. Sanasto on valittu koska se sisältää myös sanojen frekvenssit. Ilman frekvenssejä ohjelma saattaisi ehdottaa harvinaisia tai muuten outoja sanoja.
