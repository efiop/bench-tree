@0x934efea7f017fff0;

struct TreeEntry {
	key @0 :Text;
	oid @1 :Text;
}

struct Tree {
	entries @0 :List(TreeEntry);
}
