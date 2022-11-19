from ui.ohjelma import Ohjelma
from ui.konsoli_io import KonsoliIO
from entities.levenshtein import Levenshtein
from entities.trie_solmu import TrieSolmu

def main():
  io = KonsoliIO()
  sanakirja = TrieSolmu()
  sanasto = ["believe", "calendar", "caribbean", "sunday", "sitting"]
  for sana in sanasto:
    sanakirja.lisaa(sana)
  levenshtein = Levenshtein(sanakirja)
  ohjelma = Ohjelma(io, levenshtein)

  ohjelma.kaynnista()

if __name__ == "__main__":
    main()