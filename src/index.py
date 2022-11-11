from ui.app import App
from ui.konsoli_io import KonsoliIO
from levenshtein import Levenshtein

def main():
  io = KonsoliIO()
  levenshtein = Levenshtein()
  app = App(io, levenshtein)

  app.kaynnista()

if __name__ == "__main__":
    main()