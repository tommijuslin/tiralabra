# Kirjoitusvirheiden korjaaja

![GitHub Actions](https://github.com/tommijuslin/tiralabra/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/tommijuslin/tiralabra/branch/main/graph/badge.svg?token=SNMHAHCGNT)](https://codecov.io/gh/tommijuslin/tiralabra)

Tietorakenteet ja algoritmit harjoitustyö (periodi II)

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/tommijuslin/tiralabra/blob/main/dokumentaatio/maarittelydokumentti.md)
- [Testausdokumentti](https://github.com/tommijuslin/tiralabra/blob/main/dokumentaatio/testausdokumentti.md)

## Viikkoraportit

- [Viikko 1](https://github.com/tommijuslin/tiralabra/blob/main/dokumentaatio/viikko1.md)
- [Viikko 2](https://github.com/tommijuslin/tiralabra/blob/main/dokumentaatio/viikko2.md)
- [Viikko 3](https://github.com/tommijuslin/tiralabra/blob/main/dokumentaatio/viikko3.md)

## Käyttöohje

Asenna ensin riippuvuuksien hallintaan käytettävä [Poetry](https://python-poetry.org/docs/)-työkalu.

Kloonaa repo koneellesi ja asenna riippuvuudet komennolla `poetry install`.

### Käynnistäminen

Käynnistä ohjelma komennolla `poetry run python3 src/index.py`.

Käynnistykseen menee pieni hetki, sillä sanakirja muodostetaan aina uudelleen käynnistyksen yhteydessä.
