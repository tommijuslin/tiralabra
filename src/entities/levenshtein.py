class Levenshtein:
  """Luokka kahden sanan välisen etäisyyden laskemiseen ilman siirtoja."""

  def __init__(self, sanakirja):
    """Luokan konstruktori.

    Parametrit:
      sanakirja: sanat, joihin käyttäjän syöttämiä sanoja verrataan.
      sana1: vertailtava sana
      sana2: vertailtava sana
      taulu: laskemiseen käytettävä taulukko
      rivit: taulukon korkeus
      sarakkeet: taulukon leveys
    """

    self.sanakirja = sanakirja
    self.sana1 = ""
    self.sana2 = ""
    self.taulu = []
    self.rivit = 0
    self.sarakkeet = 0
  
  def etsi(self, sana, max_etaisyys):
    rivi = range(len(sana) + 1)
    sanat = []

    for kirjain in self.sanakirja.lapset:
      self.etsi_rekursiivisesti(self.sanakirja.lapset[kirjain], kirjain, sana, rivi,
        sanat, max_etaisyys)

    return sanat
  
  def etsi_rekursiivisesti(self, solmu, kirjain, sana, edellinen_rivi, sanat, max_etaisyys):
    sarakkeet = len(sana) + 1
    rivi = [edellinen_rivi[0] + 1]

    for sarake in range(1, sarakkeet):
      if sana[sarake - 1] == kirjain:
        muutos = 0
      else:
        muutos = 1

      rivi.append(min(edellinen_rivi[sarake] + 1,
                      rivi[sarake - 1] + 1,
                      edellinen_rivi[sarake - 1] + muutos))

    if rivi[-1] <= max_etaisyys and solmu.sana != None:
        sanat.append((solmu.sana, rivi[-1]))

    if min(rivi) <= max_etaisyys:
        for kirjain in solmu.lapset:
            self.etsi_rekursiivisesti(solmu.lapset[kirjain], kirjain, sana, rivi, 
                sanat, max_etaisyys)

  
  def etaisyys(self, sana1, sana2):
    """Palauttaa sanojen välisen etäisyyden.

    Parametrit:
      sana1: vertailtava sana
      sana2: vertailtava sana
    
    Palauttaa:
      sanojen välisen etäisyyden
    """
    
    self._alusta_ja_siivoa_sanat(sana1, sana2)
    self._alusta_taulu()

    return self._laske_etaisyys()
  
  def _alusta_ja_siivoa_sanat(self, sana1, sana2):
    """Muuntaa syötteet pieniksi kirjaimiksi ja poistaa välilyönnit alusta ja lopusta."""
    
    self.sana1 = sana1.strip().lower()
    self.sana2 = sana2.strip().lower()
  
  def _alusta_taulu(self):
    """Alustaa etäisyyden laskemiseen käytettävän taulukon."""

    del self.taulu[:]

    self.rivit = len(self.sana1) + 1
    self.sarakkeet = len(self.sana2) + 1

    self.taulu = [[0 for sarake in range(self.sarakkeet)] for rivi in range(self.rivit)]

    for rivi in range(1, self.rivit):
      self.taulu[rivi][0] = rivi
  
    for sarake in range(1, self.sarakkeet):
      self.taulu[0][sarake] = sarake

  def _laske_etaisyys(self):
    """Laskee sanojen välisen etäisyyden.
    
    Palauttaa:
      sanojen välisen etäisyyden
    """

    muutos = 0
    for sarake in range(1, self.sarakkeet):
      for rivi in range(1, self.rivit):
        if self.sana1[rivi-1] == self.sana2[sarake-1]:
          muutos = 0
        else:
          muutos = 1
        
        self.taulu[rivi][sarake] = min(self.taulu[rivi-1][sarake] + 1,
                                       self.taulu[rivi][sarake-1] + 1,
                                       self.taulu[rivi-1][sarake-1] + muutos)

    return self.taulu[rivi][sarake]
  
