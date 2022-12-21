from operator import itemgetter
from colorama import Fore

VAIHTOEHTOJEN_MAARA = 3


class Lauseenkorjaaja:
    """Lauseiden korjaamiseen käytettävä luokka"""

    def __init__(self, levenshtein, io):
        """Luokan konstruktori

        Parametrit:
          levenshtein: etäisyyksien laskemiseen käytettävä luokka
          io: lukemiseen ja tulostamiseen käytettävä apuluokka
        """

        self._levenshtein = levenshtein
        self._io = io

    def korjaa(self, lause):
        """Korjaa kirjoitusvirheet annetusta lauseesta

        Parametrit:
          lause: korjattava lause

        Palauttaa:
          korjatun lauseen
        """

        korjattu_lause = []

        for sana in lause:
            on_sanakirjassa = self._levenshtein.sanakirja.etsi(sana)
            if not sana.isalpha() or on_sanakirjassa[0]:
                # Tuplen toinen alkio merkkaa sanan muokatuksi.
                korjattu_lause.append((sana, False))
                continue

            vaihtoehdot = self._etsi_korjausvaihtoehdot(sana)

            if not vaihtoehdot:
                korjattu_lause.append((sana, False))
            else:
                korjattu_sana = self._korjaa_sana(sana, vaihtoehdot)
                korjattu_lause.append((korjattu_sana[0], korjattu_sana[1]))

        return korjattu_lause

    def _etsi_korjausvaihtoehdot(self, sana):
        """Etsii korjausvaihtoehdot annetulle sanalle ja järjestää ne todennäköisyyden mukaan"""

        vaihtoehdot = (self._levenshtein.etsi(sana))
        # Järjestää sanat 1. etäisyyden mukaan ja 2. frekvenssin mukaan
        vaihtoehdot.sort(key=itemgetter(2), reverse=True)
        vaihtoehdot.sort(key=itemgetter(1))

        return vaihtoehdot

    def _korjaa_sana(self, sana, vaihtoehdot):
        """Korjaa yksittäisen sanan käyttäjän valintojen perusteella

        Parametrit:
          sana: korjattava sana
          vaihtoehdot: lista korjausvaihtoehtoista
        """

        sanat = iter(vaihtoehdot)
        self._io.tulosta(f"-> {Fore.RED}{sana}{Fore.RESET} <-")

        indeksi = 0
        nayta_lisaa = True
        while True:
            if nayta_lisaa:
                self._tulosta_vaihtoehdot(sanat)
            valinta = self._io.lue("> ")
            if valinta == "q" or indeksi > len(vaihtoehdot):
                return sana, False
            if not valinta:
                indeksi += VAIHTOEHTOJEN_MAARA
                nayta_lisaa = True
                continue
            if not valinta.isdigit() or int(valinta) > VAIHTOEHTOJEN_MAARA or int(valinta) <= 0:
                self._io.tulosta("Virheellinen komento")
                nayta_lisaa = False
                continue

            return vaihtoehdot[int(valinta) + indeksi - 1][0], 1

    def _tulosta_vaihtoehdot(self, vaihtoehdot):
        """Tulostaa korjausvaihtoehdot
           Tulostettavien vaihtoehtojen määrän voi vaihtaa VAIHTOEHTOJEN_MAARA-muuttujan avulla

        Parametrit:
          vaihtoehdot: listattavat korjausvaihtoehdot
        """

        indeksi = 1
        while indeksi <= VAIHTOEHTOJEN_MAARA:
            try:
                self._io.tulosta(f"{indeksi}: {next(vaihtoehdot)[0]}")
            except StopIteration:
                self._io.tulosta(
                    f"{Fore.RED}Ei enempää vaihtoehtoja{Fore.RESET}")
                break
            indeksi += 1
        self._io.tulosta("(q: lopeta etsiminen)")
        if indeksi == VAIHTOEHTOJEN_MAARA + 1:
            self._io.tulosta("(tyhjä: lisää vaihtoehtoja)")
