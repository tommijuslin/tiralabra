from ui.ohjelma import Ohjelma
from ui.konsoli_io import KonsoliIO
from sanakirja import alusta_sanakirja
from entities.levenshtein import Levenshtein
from entities.lauseenkorjaaja import Lauseenkorjaaja


def main():
    io = KonsoliIO()

    io.tulosta("Ladataan sanoja sanakirjaan...")
    levenshtein = Levenshtein(alusta_sanakirja())
    lauseenkorjaaja = Lauseenkorjaaja(levenshtein, io)

    ohjelma = Ohjelma(io, levenshtein, lauseenkorjaaja)
    ohjelma.kaynnista()


if __name__ == "__main__":
    main()
