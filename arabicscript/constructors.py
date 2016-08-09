def arabic():
    """Arabic: 0600 — 06FF, Unicode 9.0"""
    characters = set()
    for x in range(0x0600, (0x06FF + 1)):
        characters.add(chr(x))
    characters.remove(chr(0x061D))
    return characters


def arabic_supplement():
    # Arabic Supplement: 0750 — 077F, Unicode 9.0
    characters = set()
    for x in range(0x0750, (0x077F + 1)):
        characters .add(chr(x))
    return characters


def arabic_extended_A():
    """Arabic Extended-A: 08A0 — 08FF, Unicode 9.0"""
    characters = set()
    for x in range(0x08A0, (0x08BD + 1)):
        characters.add(chr(x))
    characters .remove(chr(0x08B5))
    for x in range(0x08D4, (0x08FF + 1)):
        characters .add(chr(x))
    return characters


def arabic_presentation_forms_A():
    """Arabic Presentation Forms-A: FB50 — FDFF, Unicode 9.0"""
    characters = set()
    for x in range(0xFB50, (0xFBC1 + 1)):
        characters.add(chr(x))
    for x in range(0xFBD3, (0xFD3F + 1)):
        characters.add(chr(x))
    for x in range(0xFD50, (0xFD8F + 1)):
        characters.add(chr(x))
    for x in range(0xFD92, (0xFDC7 + 1)):
        characters.add(chr(x))
    for x in range(0xFDF0, (0xFDFD + 1)):
        characters.add(chr(x))
    return characters


def arabic_presentation_forms_B():
    """Arabic Presentation Forms-B: FE70 — FEFF, Unicode 9.0"""
    characters = set()
    for x in range(0xFE70, (0xFEFF + 1)):
        characters.add(chr(x))
    characters.remove(chr(0xFE75))
    characters.remove(chr(0xFEFD))
    characters.remove(chr(0xFEFE))
    return characters


def rumi_numeral_symbols():
    """Rumi Numeral Symbols: 10E60 — 10E7F, Unicode 9.0"""
    characters = set()
    for x in range(0x10E60, (0x10E7E + 1)):
        characters.add(chr(x))
    return characters


def arabic_mathematical_alphabetic_symbols():
    """Arabic Mathematical Alphabetic Symbols: 1EE00 — 1EEFF, Unicode 9.0"""
    characters = set()

    # individual characters
    chars = {0x1EE21, 0x1EE22, 0x1EE24, 0x1EE27, 0x1EE39, 0x1EE3B, 0x1EE42, 0x1EE47, 0x1EE49,
             0x1EE4B, 0x1EE51, 0x1EE52, 0x1EE54, 0x1EE57, 0x1EE59, 0x1EE5B, 0x1EE5D, 0x1EE5F,
             0x1EE61, 0x1EE62, 0x1EE64, 0x1EE7E, 0x1EEF0, 0x1EEF1}

    # character ranges
    ranges = {0x1EE00: 0x1EE03, 0x1EE05: 0x1EE1F, 0x1EE29: 0x1EE32, 0x1EE34: 0x1EE37,
              0x1EE4D: 0x1EE4F, 0x1EE67: 0x1EE6A,
              0x1EE6C: 0x1EE72,
              0x1EE74: 0x1EE77,
              0x1EE79: 0x1EE7C,
              0x1EE80: 0x1EE89,
              0x1EE8B: 0x1EE9B,
              0x1EEA1: 0x1EEA3,
              0x1EEA5: 0x1EEA9,
              0x1EEAB: 0x1EEBB
              }
    # add individual characters and character ranges to the collection
    for c in chars:
        characters.add(chr(c))

    for key, value in ranges.items():
        for x in range(key, (value + 1)):
            characters.add(chr(x))

    return characters


def meem_like(self):
    meems = {0x0645, # meem
             0x06D8, # small high meem initial form
             0x06E2, # small high meem isolated form
             0x06ED, # small low meem
             0x06FE, # Sindhi postposition men
             0x0765,  # meem with dot above
             0x0766,  # meem with dot below
             0x08A7,  # meem with three dots above
             0xFEE1,  # meem isolated form
             0xFEE2,  # meem final form
             0xFEE3,  # meem initial form
             0xFEE4,  # meem medial form
             0x1EE0C, # mathematical meem
             0x1EE2C, # mathematical initial meem
             0x1EE8C, # mathematical looped meem
             0x1EEAC, # mathematical double-struck meem
             }
    return {chr(c) for c in meems}

semicolons = {
    0x003B,  # SEMICOLON
    0x061B,  # ARABIC SEMICOLON
    0x204F,  # REVERSED SEMICOLON
    0x1364,  # ETHIOPIC SEMICOLON
    0xA6F6,  # BAMUM SEMICOLON
    0xFF1B,  # FULL-WIDTH SEMICOLON
    0xFE14,  # PRESENTATION FORM FOR VERTICAL SEMICOLON
    0xFE54,  # SMALL SEMICOLON
}

question_marks = {
    0x003F,  # Question mark
    0x00BF,  # Inverted question mark
    0x037E,  # Greek question mark (similar to semicolon)
    0x055E,  # Armenian question mark
    0x061F,  # Arabic question mark
    0x1367,  # Ethiopic question mark
    0x1945,  # Limbu question mark
    0x2047,  # Double question mark
    0x2048,  # Question exclamation mark
    0x2049,  # Exclamation question mark
    0x2753,  # BLACK QUESTION MARK ORNAMENT
    0x2754,  # WHITE QUESTION MARK ORNAMENT
    0x2E2E,  # Reversed question mark
    0xA60F,  # VAI QUESTION MARK
    0xA6F7,  # BAMUM QUESTION MARK
    0xFE16,  # PRE­SEN­TA­TI­ON FORM FOR VER­TI­CAL QUESTION MARK
    0xFE56,  # Small question mark
    0xFF1F,  # FULLWIDTH QUESTION MARK
    0x11143,  # CHAKMA QUESTION MARK
    0xE003F,  # TAG QUESTION MARK
}
