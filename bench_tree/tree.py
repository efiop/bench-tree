from abc import ABC

class Tree(ABC):
    def add(self, key, oid):
        pass

    def digest(self):
        pass

    @classmethod
    def from_byts(cls, byts):
        pass

    def __iter__(self):
        pass

