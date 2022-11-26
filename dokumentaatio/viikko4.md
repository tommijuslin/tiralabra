# Viikkoraportti 4

:watch: 15 tuntia

## Mitä tein tällä viikolla?

- Editointietäisyyksien laskemiseen käytettävä algoritmi tukee nyt myös siirtoja (Damerau-Levenshtein).
  - Käytössä on algoritmin rajatumpi versio, eli ns. *optimal string alignment distance*.
- Käyttäjä voi syöttää yhden sanan sijaan kokonaisia lauseita.
- Käyttöliittymää viilattu
  - Käyttöliittymä korostaa korjattuja sanoja värityksen avulla. Ominaisuutta ei ole testattu Windows-koneilla.
- Käyttöliittymän ja `Levenshtein`-luokan väliin laitettu service-luokka. Jouduin käsittelemään käyttäjän antamia syötteitä, eikä tälle koodille löytynyt sopivaa paikkaa.
- Toteutusdokumentin kirjoittaminen aloitettu.

## Ongelmia?

- Tila- ja aikavaatimusten selvittäminen. Vaikeita juttuja minulle.

## Seuraavan viikon suunnitelma

Saavutettujen tila- ja aikavaatimusten ihmettelyä. Kaikenlaista pientä refaktorointia ja optimointia. Graafinen käyttöliittymä olisi käytännöllisempi, mutta kokemusta tkinteristä ei ole.
