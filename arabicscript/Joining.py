# Refer to Arabic Shaping guide for Unicode 9.0
# http://www.unicode.org/Public/9.0.0/ucd/ArabicShaping.txt

from enum import Enum, unique


@unique
class JoiningType(Enum):
    """Joining types of unicode letters defined by the Unicode standard version 9.0"""
    Right_Joining = 1  # Letter joins with the letter to its right
    Left_Joining = 2   # Letter joins with the letter to its left
    Dual_Joining = 3   # Letter joins with letters to its left and right
    Join_Causing = 4
    Non_Joining = 5    # Letter does not join
    Transparent = 6


@unique
class JoiningGroup(Enum):
    """Joining groups of Arabic letters defined by the Unicode standard version 9.0.
    This does not include joining groups of non-Arabic scripts such as Syriac.
    """
    No_Joining_Group = 0
    Alef = 1
    Beh = 2
    Hah = 3
    Dal = 4
    Reh = 5
    Seen = 6
    Sad = 7
    Tah = 8
    Ain = 9
    Feh = 10
    Qaf = 11
    Kaf = 12
    Gaf = 13
    Lam = 14
    Meem = 15
    Noon = 16
    Heh = 17
    Waw = 18
    Yeh = 19
    Farsi_Yeh = 20
    Teh_Marbuta = 21
    Swash_Kaf = 22
    Nya = 23
    Knotted_Heh = 24
    Heh_Goal = 25
    Teh_Marbuta_Goal = 26
    Yeh_With_Tail = 27
    Yeh_Barree = 28
    Burushaski_Yeh_Barree = 29
    Rohingya_Yeh = 30
    Straight_Waw = 31
    African_Feh = 32
    African_Qaf = 33
    African_Noon = 34
