from ui.app import App
from ui.konsoli_io import KonsoliIO
from levenshtein import Levenshtein

def main():
  io = KonsoliIO()
  sanasto = ["believe", "calendar", "caribbean"]
  levenshtein = Levenshtein(sanasto)
  app = App(io, levenshtein)

  app.kaynnista()

if __name__ == "__main__":
    main()