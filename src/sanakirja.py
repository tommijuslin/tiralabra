from entities.trie_solmu import TrieSolmu

SANAKIRJA = "./words.txt"

def alusta_sanakirja():
  sanakirja = TrieSolmu()

  with open(SANAKIRJA) as sk:
    for sana in sk:
      sana = sana.split()
      sanakirja.lisaa(sana[0], int(sana[2]))
  
  return sanakirja
