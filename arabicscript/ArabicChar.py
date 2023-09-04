# -*- coding: utf-8 -*-
from .ArabChar import ArabChar

HAMZA            = 0x0621
HAMZA_HIGH       = 0x0674
HAMZA_ABOVE      = 0x0654
HAMZA_BELOW      = 0x0655

ALEF_HAMZA_ABOVE = 0x0623
WAW_HAMZA_ABOVE  = 0x0624
ALEF_HAMZA_BELOW = 0x0625
YEH_HAMZA_ABOVE  = 0x0626

ALEF       = 0x0627
ALEF_WASLA = 0x0671
ALEF_MADDA = 0x0622

BEH = 0x0628

TEH_MARBUTA = 0x0629
TEH         = 0x062A
THEH        = 0x062B

JEEM = 0x062C
HAH  = 0x062D
KHAH = 0x062E

DAL = 0x062F
ZAL = 0x0630

REH = 0x0631
ZEH = 0x0632

SEEN  = 0x0633
SHEEN = 0x0634

SAD = 0X0635
DAD = 0x0636

TAH = 0x0637
ZAH = 0x0638

AIN   = 0x0639
GHAIN = 0x063A

TATWEEL = 0x0640

FEH         = 0x0641
MAGHRIB_FEH = 0x06A2
AFRICAN_FEH = 0x08BB

QAF         = 0x0642
MAGHRIB_QAF = 0x06A7
AFRICAN_QAF = 0x08BC

KAF       = 0x0643
FARSI_KAF = 0x06A9
SWASH_KAF = 0x06AA

LAM  = 0x0644

MEEM = 0x0645

NOON         = 0x0646
AFRICAN_NOON = 0x08BD

HEH            = 0x0647
HEH_GOAL       = 0x06C1
HEH_DOCHASHMEE = 0x06BE

WAW = 0x0648

ALEF_MAKSURA = 0x0649
YEH          = 0x064A
FARSI_YEH    = 0x06CC
URDU_YEH     = 0x06D2

izlaq_letters = {
    BEH,
    REH,
    FEH,
    MAGHRIB_FEH,
    AFRICAN_FEH,
    LAM,
    MEEM,
    NOON,
    AFRICAN_NOON,
}

qalqalah_letters = {
    BEH,
    JEEM,
    DAL,
    TAH,
    QAF,
    MAGHRIB_QAF,
    AFRICAN_QAF,
}

hamza_letters = {
    HAMZA,
    HAMZA_HIGH,
    HAMZA_ABOVE,
    HAMZA_BELOW,
    ALEF_HAMZA_ABOVE,
    WAW_HAMZA_ABOVE,
    ALEF_HAMZA_BELOW,
    YEH_HAMZA_ABOVE,
}


class ArabicChar(ArabChar):
    """Class to present a character of the Arabic language, can also represent other characters
    such as space and punctuation."""
    # self._ord
    # self._chr

    def __init__(self, char):
        super(ArabicChar, self).__init__(char)

    def is_moon_letter(self):  # Ḥurūf qamrīyah
        raise NotImplementedError

    def is_sun_letter(self):  # Ḥurūf shamsīyah
        raise NotImplementedError

    def is_hamza(self):  # Any of the various shapes or carriers of hamza
        return self._ord in hamza_letters

    def is_halqi_letter(self):  # Ḥurūf ḥalqīyah
        raise NotImplementedError

    def is_tarafi_letter(self):  # Ḥurūf ṭarafīyah: Reh, Lam, Noon
        raise NotImplementedError

    def is_istela_letter(self):  # Letters with isti‘lā’
        raise NotImplementedError

    def is_izlaq_letter(self):  # Letters with Idhlāq: Beh, Reh, Feh, Lam, Meem, Noon
        return self._ord in izlaq_letters

    def is_qalqalah_letter(self):
        return self._ord in qalqalah_letters
