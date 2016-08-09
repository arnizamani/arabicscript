from unittest import TestCase

from arabicscript.Char import Char


class TestChar(TestCase):
    def test_char_eq(self):
        c1 = Char('c')
        c2  = Char('d')
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
