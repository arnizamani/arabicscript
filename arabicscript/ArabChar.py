from . import BaseForm
from .ArabicCharacters import ArabicCharacters
from .ArabicShaping import ArabicShaping
from .Char import Char
from .Joining import JoiningType, JoiningGroup
# TODO: Implement text normalization for Arabic according to Unicode normalization schemes
# TODO: Implement algorithms to find shape of a character (initial, medial, final, isolated)

_ac = ArabicCharacters()


class ArabChar(Char):
    """Class to present a character in the Arabic script, can also represent other characters
    such as space and punctuation."""
    # self._ord
    # self._chr

    def __init__(self, char):
        super(ArabChar, self).__init__(char)

    def joining_type(self):
        """Return character's joining type"""
        joining_type = ArabicShaping.joining_types.get(self._ord)
        if joining_type is None:
            joining_type = JoiningType.Non_Joining
        return joining_type

    def joining_group(self):
        """Return character's joining group"""
        joining_group = ArabicShaping.joining_groups.get(self._ord)
        if joining_group is None:
            joining_group = JoiningGroup.No_Joining_Group
        return joining_group

    def is_arabic(self):
        """Check if character exists in Unicode's Arabic code blocks"""
        return self._chr in _ac.arabic()

    def dotless_form(self):
        """Return the letter's base form, without any dots or marks"""
        b = self
        if self._chr in BaseForm.base_form:
            b = BaseForm.base_form[self._chr][0]
        return ArabChar(b)


    @DeprecationWarning
    def base_form(self):
        """Return the letter's base form, without any dots or marks"""
        b = self
        if self._chr in BaseForm.base_form:
            b = BaseForm.base_form[self._chr][0]
        return ArabChar(b)

    def is_harakat(self):
        """check if character is fatha, kasra or damma"""
        return self._ord in ArabicCharacters.harakat

    def is_tanween(self):
        """Check if character is any form of tanween"""
        return self._ord in ArabicCharacters.tanweens

    def is_sukun(self):
        """Check if character represents sukun in Arabic"""
        return self._ord in ArabicCharacters.sukun_letters

    def is_honorific(self):
        """Check if character is an honorific mark"""
        return self._ord in ArabicCharacters.honorifics

    def is_combining(self):
        """Check if the character is a combining mark"""
        return self._chr in ArabicCharacters.combining_marks
