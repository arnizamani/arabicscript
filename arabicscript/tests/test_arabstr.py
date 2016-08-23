from unittest import TestCase

from arabicscript.Joining import JoiningForm
from arabicscript.ArabStr import ArabStr


class TestArabStr(TestCase):
    def test_joining_form(self):
        string = ArabStr('ما شاء ٱلله لا قوة إلا بٱلله')
        # Ma
        self.assertEqual(string.joining_form(0), JoiningForm.Initial)  # Meem
        self.assertEqual(string.joining_form(1), JoiningForm.Final)  # Alef
        self.assertEqual(string.joining_form(2), JoiningForm.No_Joining_Form)  # Space
        # Sha'
        self.assertEqual(string.joining_form(3), JoiningForm.Initial)  # Sheen
        self.assertEqual(string.joining_form(4), JoiningForm.Final)  # Alef
        self.assertEqual(string.joining_form(5), JoiningForm.Isolated)  # Hamza
        # Allah
        self.assertEqual(string.joining_form(7), JoiningForm.Isolated)  # Alef
        self.assertEqual(string.joining_form(8), JoiningForm.Initial)  # Lam
        self.assertEqual(string.joining_form(9), JoiningForm.Medial)  # Lam
        self.assertEqual(string.joining_form(10), JoiningForm.Final)  # Heh
        # La
        self.assertEqual(string.joining_form(12), JoiningForm.Initial)  # Lam
        self.assertEqual(string.joining_form(13), JoiningForm.Final)  # Alef
        # Quwwata
        self.assertEqual(string.joining_form(15), JoiningForm.Initial)  # Qaf
        self.assertEqual(string.joining_form(16), JoiningForm.Final)  # Waw
        self.assertEqual(string.joining_form(17), JoiningForm.Isolated)  # Teh Marbuta
        # Illa
        self.assertEqual(string.joining_form(19), JoiningForm.Isolated)  # Alef with hamza below
        self.assertEqual(string.joining_form(20), JoiningForm.Initial)  # Lam
        self.assertEqual(string.joining_form(21), JoiningForm.Final)  # Alef
        # Billah
        self.assertEqual(string.joining_form(23), JoiningForm.Initial)  # Beh
        self.assertEqual(string.joining_form(24), JoiningForm.Final)  # Alef wasla
        self.assertEqual(string.joining_form(25), JoiningForm.Initial)  # Lam
        self.assertEqual(string.joining_form(26), JoiningForm.Medial)  # Lam
        self.assertEqual(string.joining_form(27), JoiningForm.Final)  # Heh
