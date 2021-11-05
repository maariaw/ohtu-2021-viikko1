import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        negVarasto = Varasto(-2)
        self.assertAlmostEqual(negVarasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        negVarasto = Varasto(10, -5)
        self.assertAlmostEqual(negVarasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-6)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_tilavuutta_suurempi_lisays_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(25)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_ottaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(-7)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negatiivinen_ottaminen_palauttaa_nolla(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)

        self.assertAlmostEqual(saatu_maara, 0)

    def test_saldon_ylittava_ottaminen_palauttaa_saldon(self):
        self.varasto.lisaa_varastoon(3)

        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(saatu_maara, 3)

    def test_saldon_ylittava_ottaminen_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(3)

        saatu_maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_merkkijonoesitys_on_odotetunlainen(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")