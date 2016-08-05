import ArabicShaping

from Char import Char
from ArabicCharacters import ArabicCharacters
from JoiningGroup import JoiningType, JoiningGroup

class ArabicChar(Char):
    # self._ord
    # self._chr
    _ac = ArabicCharacters()

    def __init__(self, char):
        super(ArabicChar, self).__init__(char)

    def joining_type(self):
        joining_type = ArabicShaping.joining_types.get(self._ord)
        if joining_type is None and self._chr in ArabicChar._ac.arabic_presentation_forms():
            joining_type = JoiningType.Non_Joining
        return joining_type

    def joining_group(self):
        joining_group = ArabicShaping.joining_groups.get(self._ord)
        if joining_group is None and self._chr in ArabicChar._ac.arabic_presentation_forms():
            joining_group = JoiningGroup.No_Joining_Group
        return joining_group

    def is_arabic(self):
        return self._chr in ArabicChar._ac.arabic()
