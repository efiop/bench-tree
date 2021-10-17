from ..tree import Tree

class Tree(Tree):
    def __init__(self):
        self.byts = None
        self._entries = []

    def add(self, key, oid):
        self._entries.append((key, oid))

    def digest(self):
        import json
        import io

        self.byts = json.dumps(self._entries).encode("utf-8")

    @classmethod
    def from_bytes(cls, byts):
        import json
        import io

        inp = io.StringIO(byts.decode("utf-8"))

        tree = cls()
        tree._entries = json.load(io.StringIO(byts.decode("utf-8")))

        tree.byts = byts
        return tree

    def as_bytes(self):
        return self.byts
