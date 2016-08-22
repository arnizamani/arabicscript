from . import constructors


class ArabicCharacters(object):
    """Functions returning collections of Arabic characters, for Unicode 9.0"""

    combining_marks = constructors.combining_marks()

    def __init__(self):
        """ArabicCharacters(): pre-construct all sets of characters"""
        self._arabic = constructors.arabic()
        self._arabic_supplement = constructors.arabic_supplement()
        self._arabic_extended_A = constructors.arabic_extended_A()
        self._arabic_presentation_forms_A = constructors.arabic_presentation_forms_A()
        self._arabic_presentation_forms_B = constructors.arabic_presentation_forms_B()
        self._arabic_presentation_forms = set.union(self._arabic_presentation_forms_A, self._arabic_presentation_forms_B)
        self._rumi_numeral_symbols = constructors.rumi_numeral_symbols()
        self._arabic_mathematical_alphabetic_symbols = \
            constructors.arabic_mathematical_alphabetic_symbols()

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
                 0xFEE1, 0xFEE2, 0xFEE3, 0xFEE4,      # Arabic presentation forms B
                 0x1EE0C, 0x1EE2C, 0x1EE8C, 0x1EEAC,  # Mathematical alphabetic symbols
                 }
        return {chr(c) for c in meems}

    honorifics = {0x0610, 0x0611, 0x0612, 0x0613, 0x0614}

    sukun_letters = {0x0652,  # Sukun
                     0x06E1,  # Dotless head of khah
                     0x08FF,  # Sideways noon ghunna
                     }

    waqf_signs = {0x0615,  # Small high tah
                  0x0617,  # Small high zain
                  0x061E,  # Triple dot punctuation mark
                  0x06D6,  # Small high salay
                  0x06D7,  # Small high qalay
                  0x06D8,  # Small high meem initial form
                  0x06D9,  # Small high lam alef
                  0x06DA,  # Small high jeem
                  0x06DB,  # Small high three dots
                  0x06DC,  # Small high seen
                  0x08D5,  # Small high sad
                  0x08D7,  # Small high qaf
                  0x08DD,  # Small high word sakta
                  0x08DE,  # Small high word qif
                  0x08DF,  # Small high word waqfa
                  }

    harakat = {0x0618,  # Small fatha
               0x0619,  # Small damma
               0x061A,  # Small kasra
               0x064E,  # Fatha
               0x064F,  # Damma
               0x0650,  # Kasra
               0x08E4,  # Curly fatha
               0x08E5,  # Curly damma
               0x08E6,  # Curly kasra
               }

    tanweens = {0x064B,  # Fathatan
                0x064C,  # Dammatan
                0x064D,  # Kasratan
                0x08E7,  # Curly fathatan
                0x08E8,  # Curly dammatan
                0x08E9,  # Curly kasratan
                0x08F0,  # Open fathatan
                0x08F1,  # Open dammatan
                0x08F2,  # Open kasratan
                }

    shadda = {0x0651}
