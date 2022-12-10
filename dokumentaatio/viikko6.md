# Viikkoraportti 6

:watch: 1 tunti

Kirjoitin kattavammat testit etäisyyksien laskemiselle. Lisäksi ohjelma toimii nyt paremmin, jos syöte sisältää välimerkkejä: sanoja ei enää esimerkiksi merkata virheellisiksi, jos ne sisältävät välimerkkejä.

## Mitä teen ensi viikolla?

Olen itse ohjelmaan tällä hetkellä tyytyväinen, mutta pari asiaa pitäisi vielä korjata.
- Käyttäjän lisäämät sanat pitäisi kirjoittaa (erilliseen?) tiedostoon, sillä tällä hetkellä ne tallennetaan tietorakenteeseen vain suorituksen ajaksi.
- `LevenshteinService`-luokasta tuli erilainen kun alunperin oli tarkoituksena. Luokka sisältää nyt myös jonkin verran käyttöliittymäkoodia, mistä en pidä.

Dokumentointi pitäisi myös saada kuntoon.
