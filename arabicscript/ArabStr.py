from .ArabChar import ArabChar


class ArabStr(object):
    """Class that represents strings containing Arabic text in Unicode"""

    def __init__(self, string=""):
        """Intialize ArabicStr from a regular string or another ArabicStr object"""
        if isinstance(string, str):
            self._str = [ArabChar(s) for s in string]
        elif isinstance(string, ArabStr):
            self._str = string._str
        else:
            raise ValueError()

    def base_form(self):
        """Convert all characters to their dotless forms"""
        result = ArabStr()
        result._str = [c.base_form() for c in self._str ]
        return result

    def __str__(self):
        """Convert to string and return"""
        result = [str(c) for c in self._str]
        return ''.join(result)

    def __repr__(self):
        result = [str(c) for c in self._str]
        return ''.join(result)

    def __len__(self):
        return len(self._str)

    def __bool__(self):
        return len(self._str) != 0

    def __contains__(self, item):
        return item in self._str

    def __eq__(self, other):
        if isinstance(other, ArabStr):
            return self._str == other._str

        if isinstance(other, str):
            return str(self) == other