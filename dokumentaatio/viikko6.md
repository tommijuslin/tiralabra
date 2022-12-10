# Viikkoraportti 6

:watch: 4 tuntia

- Poistin koko `LevenshteinService`-luokan ja siirsin suurimman osan sen sisältämästä koodista uuteen `Lauseenkorjaaja`-luokkaan.
  - Luokka oli huonosti nimetty
  - Luokasta tuli erilainen kuin oli alunperin tarkoituksena
- Kirjoitin kattavammat testit etäisyyksien laskemiselle.
- Ohjelma toimii nyt paremmin, jos syöte sisältää välimerkkejä: sanoja ei enää esimerkiksi merkata virheellisiksi, jos ne sisältävät välimerkkejä.
- Yksinkertainen validointi syötteelle, kun käyttäjä valitsee listasta haluamansa sanan
- Dokumentointia

## Mitä teen ensi viikolla?

Olen itse ohjelmaan tällä hetkellä tyytyväinen, mutta pari asiaa pitäisi vielä korjata.
- Käyttäjän lisäämät sanat pitäisi kirjoittaa (erilliseen?) tiedostoon, sillä tällä hetkellä ne tallennetaan tietorakenteeseen vain suorituksen ajaksi.
- `Lauseenkorjaaja`-luokassa on seassa käyttöliittymäkoodia, mistä en pidä. Katsotaan, jos keksisin tähän jonkun hyvän ratkaisun.

Dokumentointi pitäisi myös saada kuntoon.
