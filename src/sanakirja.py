import os
from entities.trie_solmu import TrieSolmu

SANAKIRJA = "./sanasto.txt"
KAYTTAJAN_SANAT = "./kayttajan_sanat.txt"


def alusta_sanakirja():
    sanakirja = TrieSolmu()

    lisaa_sanat_sanakirjaan(SANAKIRJA, sanakirja)
    if os.path.exists(KAYTTAJAN_SANAT):
        lisaa_sanat_sanakirjaan(KAYTTAJAN_SANAT, sanakirja)

    return sanakirja

def lisaa_sanat_sanakirjaan(tiedosto, sanakirja):
    with open(tiedosto, encoding="utf-8") as sanasto:
        for sana in sanasto:
            sana = sana.split()
            sanakirja.lisaa(sana[0], int(sana[2]))

def kirjoita_lisatyt_sanat_tiedostoon(sanat):
    if not os.path.exists(KAYTTAJAN_SANAT):
        open(KAYTTAJAN_SANAT, 'w', encoding="utf-8").close()

    with open(KAYTTAJAN_SANAT, 'a', encoding="utf-8") as sanasto:
        for sana in sanat:
            sanasto.write(f"{sana} 0 0 100000\n")
