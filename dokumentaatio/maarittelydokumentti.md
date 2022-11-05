# Määrittelydokumentti

- Opinto-ohjelma: tietojenkäsittelytieteen kandidaatti (TKT)
- Dokumentaation kieli: suomi
- Ohjelmointikieli: python
- Vertaisarvioitavaksi mieluiten pythonilla kirjoitettuja töitä mutta javakin käy pienellä varauksella.

## Aihe

Toteutetaan kirjoitusvirheiden korjaaja. Ohjelma toimii kutakuinkin näin: käyttäjä syöttää ohjelmalle lauseen tarkasteltavaksi. Sanat, jotka eivät löydy sanastosta, merkataan virheellisiksi. Virheelliset sanat korjataan editointietäisyyksien perusteella ja korjattu teksti tulostetaan käyttäjälle.

## Tietorakenteet ja algoritmit

Käyttäjän syöttämien sanojen ja sanastosta löytyvien sanojen eroavaisuudet selvitetään laskemalla niiden Damerau-Levenshteinin etäisyys. Sanaston talletukseen käytetään trie-tietorakennetta. Trien käyttö säästää paljon aikaa sellaisissa tapauksissa, missä sanat ovat hyvin samankaltaisia. Jos laskemme esimerkiksi ensin sanojen [koira, kissat] editointietäisyys ja sen jälkeen sanojen [koirat, kissat] editointietäisyys, suurin osa työstä on jo tehty ensimmäisen tapauksen jälkeen.

Kirjoitusvirheiden korjaamiseen löytyy muitakin tapoja, mutta tämän kurssin puitteisiin muut tavat vaikuttivat liian monimutkaisilta tai muuten ongelmallisilta.

## Aika- ja tilavaativuudet

Tavoitteena on laskea Damerau-Levenshteinin etäisyys ajassa O(*W*\**N*), missä *W* on pisimmän sanan pituus ja *N* solmujen määrä triessä.

## Lähteet

[Trie-tietorakenne](https://en.wikipedia.org/wiki/Trie)

[Damerau-Levenshteinin etäisyys](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)

[Steve Hanovin blogi](http://stevehanov.ca/blog/?id=114)
