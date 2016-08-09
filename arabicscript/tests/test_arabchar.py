from unittest import TestCase

from arabicscript.ArabChar import ArabChar


class TestArabChar(TestCase):
    def test_honorific(self):
        self.assertTrue(ArabChar(0x0610).is_honorific())
        self.assertTrue(ArabChar(0x0614).is_honorific())
        self.assertFalse(ArabChar(0x0615).is_honorific())
