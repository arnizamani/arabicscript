import constructors

class ArabicCharacters(object):
    """Functions returning collection of characters, for Unicode 9.0"""

    def __init__(self):
        """ArabicCharacters(): pre-construct all sets of characters"""
        self._arabic = constructors._arabic()
        self._arabic_supplement = constructors._arabic_supplement()
        self._arabic_extended_A = constructors._arabic_extended_A()
        self._arabic_presentation_forms_A = constructors._arabic_presentation_forms_A()
        self._arabic_presentation_forms_B = constructors._arabic_presentation_forms_B()
        self._arabic_presentation_forms = set.union(self._arabic_presentation_forms_A, self._arabic_presentation_forms_B)
        self._rumi_numeral_symbols = constructors._rumi_numeral_symbols()
        self._arabic_mathematical_alphabetic_symbols = \
            constructors._arabic_mathematical_alphabetic_symbols()

        self.unicode_arabic_chars = set.union(
            self._arabic,
            self._arabic_supplement,
            self._arabic_extended_A,
            self._arabic_presentation_forms,
            self._rumi_numeral_symbols,
            self._arabic_mathematical_alphabetic_symbols
        )

    def arabic(self):
        return self._arabic

    def arabic_supplement(self):
        return self._arabic_supplement

    def arabic_extended_A(self):
        return self._arabic_extended_A

    def arabic_presentation_forms_A(self):
        return self._arabic_presentation_forms_A

    def arabic_presentation_forms_B(self):
        return self._arabic_presentation_forms_B

    def arabic_presentation_forms(self):
        return self._arabic_presentation_forms

    def rumi_numeral_symbols(self):
        return self._rumi_numeral_symbols

    def arabic_mathematical_alphabetic_symbols(self):
        return self._arabic_mathematical_alphabetic_symbols

    def base_arabic_characters(self):
        """Return a set containing all Arabic characters included in Unicode standard version 9.0"""
        characters = set()
        characters.update(self._arabic)
        characters.update(self.arabic_supplement())
        characters.update(self.arabic_extended_A())
        characters.update(self.arabic_presentation_forms_A())
        characters.update(self.arabic_presentation_forms_B())
        characters.update(self.rumi_numeral_symbols())
        characters.update(self.arabic_mathematical_alphabetic_symbols())
        return characters

    def meem_like(self):
        meems = {0x0645, 0x06D8, 0x06E2, 0x06ED, 0x06FE,
                 0x0765, 0x0766, 0x08A7,
                 0xFEE1, 0xFEE2, 0xFEE3, 0xFEE4, # Arabic presentation forms B
                 0x1EE0C, 0x1EE2C, 0x1EE8C, 0x1EEAC, # Mathematical alphabetic symbols
                 }
        return {chr(c) for c in meems}

