from ui.ohjelma import Ohjelma
from ui.konsoli_io import KonsoliIO
from entities.levenshtein import Levenshtein

def main():
  io = KonsoliIO()
  sanasto = ["believe", "calendar", "caribbean"]
  levenshtein = Levenshtein(sanasto)
  ohjelma = Ohjelma(io, levenshtein)

  ohjelma.kaynnista()

if __name__ == "__main__":
    main()