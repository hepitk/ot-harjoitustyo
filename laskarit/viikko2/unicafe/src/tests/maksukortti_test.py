import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
            
    def test_rahan_laataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(90)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_saldo_vahenee_oikein_jos_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")
    
    def test_saldo_vahenee_oikein_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(11)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_true_jos_rahat_riittavat(self):
        muoto = self.maksukortti.ota_rahaa(9)
        self.assertEqual(muoto, True)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):
        muoto = self.maksukortti.ota_rahaa(11)
        self.assertEqual(muoto, False)
