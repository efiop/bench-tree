import pytest

import bench_tree.flatbuffers as fbstree
import bench_tree.json as jsontree
import bench_tree.msgpack as msgtree
import bench_tree.cfbs as cfbstree


def _build(cls):
    tree = cls()

    for i in range(1, 10**6):
        tree.add(str(i), str(i))

    tree.digest()

    return tree


@pytest.mark.parametrize(
    "cls", 
    [
        pytest.param(fbstree.Tree, id="flatbuffers"),
        pytest.param(jsontree.Tree, id="json"),
        pytest.param(msgtree.Tree, id="msgpack"),
#        pytest.param(cfbstree.Tree, id="cfbs"),
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
#        pytest.param(cfbstree.Tree, id="cfbs"),
    ]
)
def test_load(benchmark, cls):
    tree = _build(cls)
    byts = tree.as_bytes()
    benchmark(tree.from_bytes, byts)
