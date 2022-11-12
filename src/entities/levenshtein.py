class Levenshtein:
  """Luokka kahden sanan välisen (editointi)etäisyyden laskemiseen ilman siirtoja."""

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
  
  def etsi(self, syote, max_etaisyys):
    """Etsii sanat, joiden etäisyys annettuun sanaan on enintään annettu maksimietäisyys.

    Parametrit:
      syote: etsittävä sana
      max_etaisyys: sanojen maksimietäisyys etsittävästä sanasta
    
    Palauttaa:
      listan löydetyistä sanoista

    """
    sanat = []

    for kohdesana in self.sanakirja:
      etaisyys = self.etaisyys(syote, kohdesana)
      if etaisyys <= max_etaisyys:
        sanat.append([kohdesana, etaisyys])
      
    return sanat
  
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
  
