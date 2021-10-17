import msgpack

from ..tree import Tree


class Tree(Tree):
    def __init__(self):
        self.fbs = None
        self.byts = None
        self._entries = []

    def add(self, key, oid):
        self._entries.append((key, oid))

    def digest(self):
        self.byts = msgpack.packb([1, 2, 3], use_bin_type=True)

    @classmethod
    def from_bytes(cls, byts):
        tree = cls()
        msgpack.unpackb(byts, use_list=False, raw=False)
        tree.byts = byts
        return tree

    def as_bytes(self):
        return self.byts
