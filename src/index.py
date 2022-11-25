from ui.ohjelma import Ohjelma
from ui.konsoli_io import KonsoliIO
from entities.levenshtein import Levenshtein
from entities.trie_solmu import TrieSolmu

SANAKIRJA = "./words.txt"

def main():
  io = KonsoliIO()
  sanakirja = TrieSolmu()

  io.tulosta("Ladataan sanoja sanakirjaan...")
  alusta_sanakirja(sanakirja)

  levenshtein = Levenshtein(sanakirja)
  ohjelma = Ohjelma(io, levenshtein)

  ohjelma.kaynnista()

def alusta_sanakirja(sanakirja):
  with open(SANAKIRJA) as sk:
    for sana in sk:
      sana = sana.split()
      sanakirja.lisaa(sana[0], int(sana[2]))

if __name__ == "__main__":
    main()