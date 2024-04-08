################################## WITHOUT DATACLASS ##################################

from functools import total_ordering
@total_ordering
class ManualComment:
    def __init__(self, id, text):
        self.__id = id
        self.__text = text

    @property
    def id(self):
        return self.__id

    @property
    def text(self):
        return self.__text

    def __repr__(self):
        return f"ManualComment({self.__class__.__name__} ,{self.__id}, {self.__text})"

    def __eq__(self, other: object):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __hash__(self):
        return hash((self.__class__ ,self.id, self.text))

    def __lt__(self, other: object):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other: object):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other: object):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other: object):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented


if __name__ == "__main__":
    print(ManualComment(1, "abc"))
    print(ManualComment(2, "def"))
    print(ManualComment(1, "abc") == ManualComment(1, "abc"))
    print(ManualComment(1, "abc") == ManualComment(2, "abc"))
    print(ManualComment(1, "abc") < ManualComment(2, "abc"))


################################## WITHOUT DATACLASS ##################################


