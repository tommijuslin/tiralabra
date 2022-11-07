from ui.app import App
from ui.konsoli_io import KonsoliIO

def main():
  io = KonsoliIO()
  app = App(io)

  app.kaynnista()

if __name__ == "__main__":
    main()