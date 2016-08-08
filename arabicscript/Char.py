# -*- coding: utf-8 -*-
import unicodedata


class InvalidCharacter(Exception):
    pass


class Char(object):
    """Unicode character"""
    _semicolons = {
        0x003B,  # SEMICOLON
        0x061B,  # ARABIC SEMICOLON
        0x204F,  # REVERSED SEMICOLON
        0x1364,  # ETHIOPIC SEMICOLON
        0xA6F6,  # BAMUM SEMICOLON
        0xFF1B,  # FULL-WIDTH SEMICOLON
        0xFE14,  # PRESENTATION FORM FOR VERTICAL SEMICOLON
        0xFE54,  # SMALL SEMICOLON
    }

    def __init__(self, char):
        self._ord = -1
        self._chr = ''

        if isinstance(char, int):
            if char >= 0:
                self._ord = char
                self._chr = chr(self._ord)
                return
            else:
                raise InvalidCharacter()

        if isinstance(char, Char):
            self._chr = char._chr
            self._ord = char._ord
            return

        if not char or not isinstance(char, str) or len(char) > 1:
            raise InvalidCharacter()

        self._chr = char
        self._ord = ord(self._chr)

    def name(self):
        """Returns the unicode name of the character, or empty string"""
        return unicodedata.name(self._chr, "")

    # Boolean methods
    def isalnum(self):
        return self._chr.isalnum()

    def isalpha(self):
        return self._chr.isalpha()

    def isdecimal(self):
        return self._chr.isdecimal()

    def isdigit(self):
        return self._chr.isdigit()

    def islower(self):
        return self._chr.islower()

    def isnumeric(self):
        return self._chr.isnumeric()

    def isprintable(self):
        return self._chr.isprintable()

    def isspace(self):
        return self._chr.isspace()

    def istitle(self):
        return self._chr.istitle()

    def isupper(self):
        return self._chr.isupper()

    def issemicolon(self):
        return self._ord in Char._semicolons

    # Builtin methods
    def __str__(self):
        return self._chr

    def __repr__(self):
        return self._chr

    def __hash__(self):
        return hash(self._ord)

    def __bool__(self):
        return self._ord > 0

    def __int__(self):
        """Returns integer value of the digit"""
        return int(self._chr)

    def __eq__(self, other):
        if isinstance(other, str):
            return self._chr == other

        if isinstance(other, int):
            return self._ord == other

        if isinstance(other, Char):
            return self._ord == other._ord

    def __lt__(self, other):
        return self._ord < other._ord

    def __gt__(self, other):
        return self._ord > other._ord

    def __le__(self, other):
        return self._ord <= other._ord

    def __ge__(self, other):
        return self._ord >= other._ord