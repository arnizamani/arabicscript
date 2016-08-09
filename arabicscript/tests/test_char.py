from unittest import TestCase

from arabicscript.Char import Char, InvalidCharacter
from arabicscript.ArabChar import ArabChar


class TestChar(TestCase):
    def test_char_init(self):
        a = Char('a')
        b = ArabChar('ب')
        self.assertRaises(InvalidCharacter, lambda: Char(-1))     # negative numbers are not allowed
        self.assertRaises(InvalidCharacter, lambda: Char('ab'))   # length should be 1
        self.assertRaises(InvalidCharacter, lambda: Char(['a']))  # Only str, int and Char types are allowed

    def test_char_eq(self):
        c1 = Char('c')
        c2 = Char('d')
        c3 = Char('c')
        self.assertEqual(c1, c1)
        self.assertEqual(c1, c3)
        self.assertEqual(c1, 'c')
        self.assertNotEqual(c1, c2)
        self.assertNotEqual(c2, c3)
        self.assertNotEqual('d', c1)

    def test_char_int(self):
        self.assertEqual(int(Char('0')), 0)
        self.assertEqual(int(Char('١')), 1)
        self.assertEqual(int(Char('۲')), 2)

    def test_char_name(self):
        self.assertTrue(Char('a').name())      # An existing character returns non-empty string
        self.assertTrue(Char('ب').name())
        self.assertFalse(Char(0x08C0).name())  # A non-existing character returns empty string
