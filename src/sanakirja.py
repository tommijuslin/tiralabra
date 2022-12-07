from entities.trie_solmu import TrieSolmu

SANAKIRJA = "./sanasto.txt"

def alusta_sanakirja():
  sanakirja = TrieSolmu()

  with open(SANAKIRJA, encoding="utf-8") as sanasto:
    for sana in sanasto:
      sana = sana.split()
      sanakirja.lisaa(sana[0], int(sana[2]))

  return sanakirja
