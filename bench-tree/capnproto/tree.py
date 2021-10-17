import capnp  # noqa: F401

import tree_capnp

import flatbuffers
from ..tree import Tree

from .Tree.Tree import Tree as FBSTree, TreeStartEntriesVector, TreeStart, TreeEnd, TreeAddEntries
from .Tree.TreeEntry import TreeEntry, TreeEntryStart, TreeEntryEnd, TreeEntryAddKey, TreeEntryAddOid

class Tree(Tree):
    def __init__(self):
        self.fbs = None
        self.byts = None
        self._entries = []

    def add(self, key, oid):
        self._entries.append((key, oid))

    def digest(self):
        builder = flatbuffers.Builder(0)

        entries = []
        for key, oid in self._entries:
            key_str = builder.CreateString(key)
            oid_str = builder.CreateString(oid) 

            TreeEntryStart(builder)
            TreeEntryAddKey(builder, key_str)
            TreeEntryAddOid(builder, oid_str)
            entries.append(TreeEntryEnd(builder))

        TreeStartEntriesVector(builder, len(self._entries))
        for entry in entries:
            builder.PrependUOffsetTRelative(entry)
        entries = builder.EndVector()

        TreeStart(builder) 
        TreeAddEntries(builder, entries)
        self.fbs = TreeEnd(builder)

        builder.Finish(self.fbs)

        self.byts = builder.Output()

#    def digest(self):
#        builder = flatbuffers.Builder(100000000)
#
#        pairs = []
#        for key, oid in self._entries:
#            key_str = builder.CreateString(key)
#            oid_str = builder.CreateString(oid) 
#
#            pairs.append((key_str, oid_str))
#
#        entries = []
#        for key, oid in pairs:
#            TreeEntryStart(builder)
#            TreeEntryAddKey(builder, key_str)
#            TreeEntryAddOid(builder, oid_str)
#            entries.append(TreeEntryEnd(builder))
#
#        TreeStartEntriesVector(builder, len(self._entries))
#        for entry in entries:
#            builder.PrependUOffsetTRelative(entry)
#        entries = builder.EndVector()
#
#        TreeStart(builder) 
#        TreeAddEntries(builder, entries)
#        self.fbs = TreeEnd(builder)
#
#        builder.Finish(self.fbs)
#
#        self.byts = builder.Output()
#
    @classmethod
    def from_bytes(cls, byts):
        import io
        tree = cls()
        tree.fbs = FBSTree.GetRootAsTree(byts, 0)
        tree.byts = byts
        return tree

    def as_bytes(self):
        return self.byts
