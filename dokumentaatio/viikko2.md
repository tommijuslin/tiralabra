# Viikkoraportti 2

:watch: 10 tuntia

Kurssin alku meni aikamoiseksi haparoinniksi. Tällä viikolla palautin mieleen paljon asioita ohjelmistotekniikan materiaalin avulla.

Ohjelma on edistynyt kohtalaisesti. Kaikenlaiseen tunkkaamiseen ja ohjelman rakenteen mietiskelyyn kului paljon aikaa. Halusin saada mahdollisimman nopeasti jotain toimivaa aikaiseksi, mistä syystä käytössä on tällä hetkellä klassinen (yksinkertaisempi) Levenshteinin etäisyys ilman siirtoja. Damerau-Levenshtein -etäisyyteen siirtyminen ja Trie-tietorakenteen käyttöönotto edellyttää luultavasti suurempia refaktorointeja, mutta ihmetellään niitä sitten ensi viikolla. Editointietäisyyksien laskemiseen käytetty algoritmi on kirjoitettu wikipediasta löytyvän pseudokoodin pohjalta. Eniten vaikeuksia aiheutti algoritmin pilkkominen järkeviin osiin.

Varsinaisen ohjelman lisäksi kirjoitin levenshtein-luokalle mahdollisimman kattavat testit. Dokumentointiin meni myös jonkin verran aikaa. Dokumentointityyli pohjautuu ohjelmistotekniikan esimerkkiprojektissa käytettyyn tyyliin.

Seuraavaksi tarkoituksena on tallentaa sanasto Trie-tietorakenteeseen. Muutan myös etäisyysalgoritmin tukemaan siirtoja (Damerau-Levenshtein). Yksittäisen sanan sijaan käyttäjä voi syöttää ohjelmaan kokonaisen lauseen.
