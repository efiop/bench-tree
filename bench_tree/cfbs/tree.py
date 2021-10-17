from ..tree import Tree

from .cfbs import build, load


class Tree(Tree):
    def __init__(self):
        self.fbs = None
        self.byts = None
        self._entries = []

    def add(self, key, oid):
        self._entries.append((key, oid))

    def digest(self):
        self.fbs, self.byts = build(self._entries)

    @classmethod
    def from_bytes(cls, byts):
        import io
        tree = cls()
        tree.fbs = load(byts)
        tree.byts = byts
        return tree

    def as_bytes(self):
        return self.byts
