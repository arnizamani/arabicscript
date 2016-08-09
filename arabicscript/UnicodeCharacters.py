class UnicodeCharacters(object):
    """Functions returning collections of characters, for Unicode 9.0"""

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
        0x003E,  # Question mark
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
