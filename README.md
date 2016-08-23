# arabicscript
**arabicscript is a Python library of tools for Arabic script based on the Unicode standard.**

This version works for Unicode 9.0.

It is independant of font technology, and is intended for the script in general and not for any particular language. It provides utilities for querying properties of Arabic characters and manipulating Arabic-script strings. Some script-independent Unicode tools are also provided.

## Main classes
#### Char
Defines some general attributes of a Unicode character

#### ArabChar
Defines attributes of a Arabic-script character

*  joining_type(): returns the type of joining, e.g., Right_Joining, Left_Joining, Dual_Joining
*  joining_group(): return the character group of joining, e.g., Beh, Dal, Reh, Heh, Waw, Yeh
*  base_form(): returns the base form of the letter, that excludes any dots or other marks. E.g., base form of Beh is Dotless beh.
*  is_combining(): checks if the character is a combining character (only right combining)
#### ArabicChar
Defines additional attributes of a character used in the Arabic language

*  is_hamza(): check if character is any form of hamza (hamza, alef hamza, waw hamza, yeh hamza, etc.)
*  is_islaq_letter(): check if character has the property of Idhlāq (Quranic Arabic), i.e., Beh, Reh, Feh, Lam, Meem, Noon
*  is_qalqalah_letter(): check if letter is one of huruf qalqalah (jeem, dal, etc.)
#### ArabStr
Represents strings consisting of Arabic-script characters

*  base_form(): convert all letters in the string to their base forms
*  joining_form(index): returns the joining form of the character in its context: isolated, initial, medial, final