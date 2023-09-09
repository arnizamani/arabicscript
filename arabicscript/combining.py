"""
List of Unicode combining characters for the Arabic script.
Updated for Unicode 15.0, Sep 2022

Quranic Ayah sign is not included, since it is mostly used as an independent
character, not as a combining character.

"""

COMBINING_CHARS = [
# Subtending marks
    '\u0600', # Arabic number sign
    '\u0601', # Arabic sign sanah
    '\u0602', # Arabic footnote marker
    '\u0603', # Arabic sign safha
    '\u0604', # Arabic sign samvat
    '\u0605', # Arabic number mark above
# Honorifics
    '\u0610', # Arabic sign sallallahu
    '\u0611', # Arabic sign alayhissalam
    '\u0612', # Arabic sign rahmatullah alayh
    '\u0613', # Arabic sign radi Allahu anhu
    '\u0614', # Arabic sign Takhallus
# Quranic annotation signs
    '\u0615', # Araibc small high tah
    '\u0616', # Arabic small high ligature alef yeh
    '\u0617', # Arabic small high zain
    '\u0618', # Arabic small fatha
    '\u0619', # Arabic small damma
    '\u061A', # Arabic small kasra
# Format character
    '\u061C', # Arabic letter mark
    '\u0640', # Arabic tatweel
# Tashkil
    '\u064B', # Arabic fathatan
    '\u064C', # Arabic dammatan
    '\u064D', # Arabic kasratan
    '\u064E', # Arabic fatha
    '\u064F', # Arabic damma
    '\u0650', # Arabic kasra
    '\u0651', # Arabic shadda
    '\u0652', # Arabic sukun
# Other Combining marks
    '\u0653', # Arabic maddah above
    '\u0654', # Arabic hamza above
    '\u0655', # Arabic hamza below
    '\u0656', # Arabic superscript alef
    '\u0657', # Arabic inverted damma
    '\u0658', # Arabic mark noon ghunna
    '\u0659', # Arabic zwarakay
    '\u065A', # Arabic vowel sign small V above
    '\u065B', # Arabic vowel sign inverted small V above
    '\u065C', # Arabic vowel sign dot below
    '\u065D', # Arabic reversed damma
    '\u065E', # Arabic fatha with two dots
    '\u065F', # Arabic wavy hamza below
# Tashkil
    '\u0670', # Arabic letter superscript alef
# Quranic annotation signs
    '\u06D6', # Arabic sign sallay
    '\u06D7', # Arabic sign qalay
    '\u06D8', # Arabic high meem
    '\u06D9', # Arabic high lam alef
    '\u06DA', # Arabic high jeem
    '\u06DB', # Arabic high three dots
    '\u06DC', # Arabic high seen
    '\u06DF', # Arabic high rounded zero
    '\u06E0', # Arabic high rectangular zero
    '\u06E1', # Arabic high dotless khah
    '\u06E2', # Arabic high meem
    '\u06E3', # Arabic low seen
    '\u06E4', # Arabic high madda
    '\u06E7', # Arabic high yeh
    '\u06E8', # Arabic high noon
    '\u06EA', # Arabic empty centre low stop
    '\u06EB', # Arabic empty centre high stop
    '\u06EC', # Arabic rounded high stop filled
    '\u06ED', # Arabic low meem
# Arabic Extended-B
# Supertending currency symbols
    '\u0890', # Arabic pound mark above
    '\u0891', # Arabic piastre mark above
# Additions for Quranic orthographies
    '\u0898', # High word al-juz
    '\u0899', # Low word Ishmaam
    '\u089A', # Low word Imaala
    '\u089B', # Low word Tas'heel
    '\u089C', # Madda wajib
    '\u089D', # Superscript aelf mokhassas
    '\u089E', # Doubled madda
    '\u089F', # Half madda over madda
    # Arabic Extended-A
    '\u08CA', # High Farsi Yeh
    '\u08CB', # High Yeh Barree with dots
    '\u08CC', # High word sah (waqf sign)
    '\u08CD', # High Zah
    '\u08CE', # Large round dot above
    '\u08CF', # Large round dot below
    '\u08D0', # Sukun below
    '\u08D1', # Large circle below
    '\u08D2', # Large round dot inside circle below
    '\u08D3', # Low Waw
    '\u08D4', # High word Ar-Rub'a
    '\u08D5', # High Sad
    '\u08D6', # High Ain
    '\u08D7', # High Qaf
    '\u08D8', # High Noon with Kasra
    '\u08D9', # Low noon with kasra
    '\u08DA', # High word ath-Thalatha
    '\u08DB', # High word As-Sadja
    '\u08DC', # High word An-Nisf
    '\u08DD', # High word Sakta
    '\u08DE', # High word Qif
    '\u08DF', # High word Waqfa
    '\u08E0', # High footnote marker
    '\u08E1', # High sign safha
    '\u08E2', # Disputed end of ayah
# Vowel signs for different langauges
    '\u08E3', # Turned damma below (Arwi)
    '\u08E4', # Curly fatha (Rohingya)
    '\u08E5', # Curly damma
    '\u08E6', # Curly kasra
    '\u08E7', # Curly fathatan
    '\u08E8', # Curly dammatan
    '\u08E9', # Curly kasratan
    '\u08EA', # Tone one dot above (Rohingya)
    '\u08EB', # Tone two dots above
    '\u08EC', # Tone loop above
    '\u08ED', # Tone one dot below
    '\u08EE', # Tone two dots below
    '\u08EF', # Tone loop below
# Quranic annotation signs
    '\u08F0', # Open fathatan
    '\u08F1', # Open dammatan
    '\u08F2', # Open kasratan
    '\u08F3', # High Waw
# Extended vowel signs
    '\u08F4', # Fatha with ring
    '\u08F5', # Fatha with dot above
    '\u08F6', # Kasra with dot below
    '\u08F7', # Left arrowhead above
    '\u08F8', # Right arrowhead above
    '\u08F9', # Left arrowhead below
    '\u08FA', # Right arrowhead below
    '\u08FB', # Double right arrowhead above
    '\u08FC', # Double right arrowhead above with dot
    '\u08FD', # Right arrowhead above with dot
    '\u08FE', # Damma with dot
    '\u08FF', # Sideways noon ghunna
# Arabic Extended-C
# Quranic orthographies
    '𐻽', # \u10EFD Low word Sakta
    '𐻾', # \u10EFE Low word Qasr
    '𐻿', # \u10EFF Low word Madda
]


def remove_combining_characters(text: str) -> str:
    """Remove Arabic combining characters from the text."""
    return ''.join(['' if x in COMBINING_CHARS else x for x in text])
