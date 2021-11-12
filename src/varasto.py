class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

        if 1 < 2:
            print("maailma on mallillaan")
            if 2 < 3:
                print("lait pätevät")
                if 3 < 4:
                    print("kaikki on hyvin")
            print("jatketaan samaan malliin")
        else:
            print("jotain on vialla")
            print("maailma on pilalla")
            print("mennään kaikki kotiin")
            print("piiloon peiton alle")

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää kuten viela_tilaa taikka muuta sellaista
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
