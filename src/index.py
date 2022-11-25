from ui.ohjelma import Ohjelma
from ui.konsoli_io import KonsoliIO
from sanakirja import alusta_sanakirja
from services.levenshtein_service import LevenshteinService
from entities.levenshtein import Levenshtein
from entities.trie_solmu import TrieSolmu


def main():
  io = KonsoliIO()
  io.tulosta("Ladataan sanoja sanakirjaan...")
  levenshtein = Levenshtein(alusta_sanakirja())
  service = LevenshteinService(levenshtein)

  ohjelma = Ohjelma(io, service)
  ohjelma.kaynnista()

if __name__ == "__main__":
    main()