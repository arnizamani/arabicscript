from ArabicChar import ArabicChar

class ArabicStr(object):
    def __init__(self, string):
        self._str = [ArabicChar(s) for s in string]

    def to_base_form(self):
        for c in self._str:
            c.to_base_form()

    def __str__(self):
        result = [c.__str__() for c in self._str]
        return ''.join(result)

    def __repr__(self):
        result = [c.__str__() for c in self._str]
        return ''.join(result)

    def __len__(self):
        return len(self._str)

    def __bool__(self):
        return len(self._str) != 0

    def __contains__(self, item):
        return item in self._str

    def __eq__(self, other):
        if isinstance(other, ArabicStr):
            return self._str == other._str

        if isinstance(other, str):
            return self._str == [ArabicChar(c) for c in str]