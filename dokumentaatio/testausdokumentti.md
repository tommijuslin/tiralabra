# Testausdokumentti

[![codecov](https://codecov.io/gh/tommijuslin/tiralabra/branch/main/graph/badge.svg?token=SNMHAHCGNT)](https://codecov.io/gh/tommijuslin/tiralabra)

## Testien toistaminen

Siirry virtuaaliympäristöön komennolla `poetry shell` ja suorita komento `pytest src`.

## Yksikkötestit

### Levenshtein

Editointietäisyyksien laskemiseen käytettävää `Levenshtein`-luokkaa testataan sanapareilla, joiden väliset etäisyydet ovat ennalta tiedettyjä ja erisuuruisia. Etäisyyksien lisäksi testit testaavat luokan hakutoimintoa, joka palauttaa todennäköisimmät korjausvaihtoehdot.

### TrieSolmu

Trie-tietorakenteen toteuttavaa `TrieSolmu`-luokkaa testataan lisäämällä siihen sanoja ja tarkistamalla löytyvätkö juuri lisätyt sanat.

## Integraatiotestit

### Lauseenkorjaaja

Testeissä keskitytään erityisesti syötetyn lauseen korjauksen oikeellisuuteen. Luokan palauttama lista korjatuista sanoista sisältää tiedon siitä, onko sanoja muokattu, ja tähän on myös käyttäjällä mahdollisuus vaikuttaa: käyttäjä voi esimerkiksi päättää olla korjaamatta sanaa, jolloin ohjelma ei merkkaa sanaa muokatuksi. Testit varmistavat, että ohjelma toimii oikein erilaisissa tilanteissa käyttäjän tekemien valintojen mukaan.

## Suorituskykytestit

- Ei vielä testattu
