# Testausdokumentti

[![codecov](https://codecov.io/gh/tommijuslin/tiralabra/branch/main/graph/badge.svg?token=SNMHAHCGNT)](https://codecov.io/gh/tommijuslin/tiralabra)

## Testien toistaminen

Siirry virtuaaliympäristöön komennolla `poetry shell` ja suorita komento `pytest src`.

## Testit

### Levenshtein

Editointietäisyyksien laskemiseen käytettävää `Levenshtein`-luokkaa testataan sanapareilla, joiden väliset etäisyydet ovat ennalta tiedettyjä ja erisuuruisia. Etäisyyksien lisäksi testit testaavat luokan hakutoimintoa, joka palauttaa todennäköisimmät korjausvaihtoehdot.

### TrieSolmu

Trie-tietorakenteen toteuttavaa `TrieSolmu`-luokkaa testataan lisäämällä siihen sanoja ja tarkistamalla löytyvätkö juuri lisätyt sanat.
