import pytest

from . import flatbuffers as fbstree
from . import json as jsontree
from . import msgpack as msgtree

def _build(cls):
    tree = cls()

    for i in range(1, 10**3):
        tree.add(str(i), str(i))

    tree.digest()

    return tree


@pytest.mark.parametrize(
    "cls", 
    [
        pytest.param(fbstree.Tree, id="flatbuffers"),
        pytest.param(jsontree.Tree, id="json"),
        pytest.param(msgtree.Tree, id="msgpack"),
    ]
)
def test_build(benchmark, cls):
    benchmark(_build, cls)


@pytest.mark.parametrize(
    "cls", 
    [
        pytest.param(fbstree.Tree, id="flatbuffers"),
        pytest.param(jsontree.Tree, id="json"),
        pytest.param(msgtree.Tree, id="msgpack"),
    ]
)
def test_dump(benchmark, cls):
    tree = _build(cls)
    benchmark(tree.as_bytes)


@pytest.mark.parametrize(
    "cls", 
    [
        pytest.param(fbstree.Tree, id="flatbuffers"),
        pytest.param(jsontree.Tree, id="json"),
        pytest.param(msgtree.Tree, id="msgpack"),
    ]
)
def test_load(benchmark, cls):
    tree = _build(cls)
    byts = tree.as_bytes()
    benchmark(tree.from_bytes, byts)
