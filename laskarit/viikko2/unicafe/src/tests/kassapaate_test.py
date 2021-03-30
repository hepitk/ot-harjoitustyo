import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
        self.maksukortti2 = Maksukortti(100)

    def test_luotu_paate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodun_kassapaatteen_rahamaara_ja_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullisen_lounaan_osto_kasvattaa_kassaa_ja_maaraa_ja_vaihtoraha_oikea(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)        
        self.assertEqual(maksu, 10)
    
    def test_edullisen_lounaan_osto_ei_mene_lapi_jos_maksu_pieni(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)        
        self.assertEqual(maksu, 230)
    
    def test_maukkaan_lounaan_osto_kasvattaa_kassaa_ja_maaraa_ja_vaihtoraha_oikea(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)        
        self.assertEqual(maksu, 10)

    def test_maukkaan_lounaan_osto_ei_mene_lapi_jos_maksu_pieni(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)        
        self.assertEqual(maksu, 390)
    
    def test_edullisen_lounaan_korttiosto_toimii_jos_kortilla_tarpeeksi_rahaa(self):
        maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")
        self.assertEqual(maksu, True)
    
    def test_edullisen_lounaan_korttiosto_ei_mene_lapi__jos_kortilla_ei_tarpeeksi_rahaa(self):
        maksu = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti2), "saldo: 1.0")
        self.assertEqual(maksu, False)

    def test_maukkaan_lounaan_korttiosto_toimii_jos_kortilla_tarpeeksi_rahaa(self):
        maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")
        self.assertEqual(maksu, True)

    def test_maukkaan_lounaan_korttiosto_ei_mene_lapi_jos_kortilla_ei_tarpeeksi_rahaa(self):
        maksu = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti2)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti2), "saldo: 1.0")
        self.assertEqual(maksu, False)
    
    def test_kortille_lataus_toimii_oikein(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(str(self.maksukortti), "saldo: 11.0")

    def test_kortille_lataus_ei_mene_lapi_jos_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        
    

               


