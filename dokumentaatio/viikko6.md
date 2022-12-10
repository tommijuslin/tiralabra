# Viikkoraportti 6

:watch: 2 tuntia

- Kirjoitin kattavammat testit etäisyyksien laskemiselle.
- Ohjelma toimii nyt paremmin, jos syöte sisältää välimerkkejä: sanoja ei enää esimerkiksi merkata virheellisiksi, jos ne sisältävät välimerkkejä.
- Yksinkertainen validointi syötteelle, kun käyttäjä valitsee listasta haluamansa sanan
- Dokumentointia

## Mitä teen ensi viikolla?

Olen itse ohjelmaan tällä hetkellä tyytyväinen, mutta pari asiaa pitäisi vielä korjata.
- Käyttäjän lisäämät sanat pitäisi kirjoittaa (erilliseen?) tiedostoon, sillä tällä hetkellä ne tallennetaan tietorakenteeseen vain suorituksen ajaksi.
- `LevenshteinService`-luokasta tuli erilainen kun alunperin oli tarkoituksena. Luokka sisältää nyt myös jonkin verran käyttöliittymäkoodia, mistä en pidä.

Dokumentointi pitäisi myös saada kuntoon.
