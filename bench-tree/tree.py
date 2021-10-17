from abc import ABC

class Tree(ABC):
    def add(self, key, oid):
        pass

    @classmethod
    def from_buf(cls, byts):
        pass

    def as_buf(self):
        pass

    def __iter__(self):
        pass

