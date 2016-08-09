from . import ArabicShaping
from . import BaseForm
from .ArabicCharacters import ArabicCharacters
from .Char import Char
from .Joining import JoiningType, JoiningGroup


class ArabicChar(Char):
    # self._ord
    # self._chr
    _ac = ArabicCharacters()

    def __init__(self, char):
        super(ArabicChar, self).__init__(char)

    def joining_type(self):
        """Return character's joining type"""
        joining_type = ArabicShaping.joining_types.get(self._ord)
        if joining_type is None and self._chr in ArabicChar._ac.arabic_presentation_forms():
            joining_type = JoiningType.Non_Joining
        return joining_type

    def joining_group(self):
        """Return character's joining group"""
        joining_group = ArabicShaping.joining_groups.get(self._ord)
        if joining_group is None and self._chr in ArabicChar._ac.arabic_presentation_forms():
            joining_group = JoiningGroup.No_Joining_Group
        return joining_group

    def is_arabic(self):
        """Check if character exists in Unicode's Arabic code blocks"""
        return self._chr in ArabicChar._ac.arabic()

    def base_form(self):
        """Return the letter's base form, without any dots or marks"""
        b = self
        if self._chr in BaseForm.base_form:
            b = BaseForm.base_form[self._chr][0]
        return ArabicChar(b)

    def is_haraka(self):
        """check if character is fatha, kasra or damma"""
        raise NotImplementedError()

    def is_tanween(self):
        raise NotImplementedError()

    def is_regular_tanween(self):
        raise NotImplementedError()

    def is_sukun(self):
        raise NotImplementedError()

