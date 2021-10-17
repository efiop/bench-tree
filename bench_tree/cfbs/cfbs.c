#include <Python.h>
#include <fcntl.h>
#include <sys/syscall.h>
#include <unistd.h>

#include "tree_builder.h"
#include "tree_reader.h"

static PyObject*
_build(PyObject* self, PyObject* args) {
    PyObject *pList;
    PyObject *pItem;
    Py_ssize_t n;
    int i;

    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &pList)) {
        PyErr_SetString(PyExc_TypeError, "parameter must be a list.");
        return NULL;
    }

    n = PyList_Size(pList);
    for (i=0; i<n; i++) {
        pItem = PyList_GetItem(pList, i);
        if(!PyTuple_Check(pItem)) {
            PyErr_SetString(PyExc_TypeError, "list items must be tuples.");
            return NULL;
        }

        key = PyTuple_GetItem(pItem, 0)
        oid = PyTuple_GetItem(pItem, 1)

        key_str = PyBytes_AS_STRING(key)
        oid_str = PyBytes_AS_STRING(oid)

        key_fbs = flatbuffers_string_create_str(B, key_str)
        oid_fbs = flatbuffers_string_create_str(B, oid_str)

        ns(TreeEntry_ref_t) entry = ns(TreeEntry_create(B, key_fbs, oid_fbs));
    }

    ns(Tree_entries_start(B));
    ns(Tree_entries_push_create(B));
    ns(OC

   entries = flatbuffers_

    ns(Tree_end_as_root(B))

}


static PyObject*
_load(PyObject* self, PyObject* args) {
    Py_RETURN_NONE;

//    char* path1;
//    char* path2;
//
//    if (!PyArg_ParseTuple(args, "ss", &path1, &path2)) {
//        return NULL;
//    }
//
//    if (syscall(SYS_renameat2, AT_FDCWD, path1, AT_FDCWD, path2, RENAME_EXCHANGE)) {
//        return PyErr_SetFromErrno(PyExc_OSError);
//    } else {
//        Py_RETURN_NONE;
//    }
//
//
}


static struct PyMethodDef methods[] = {
    {"build", (PyCFunction)_build, METH_VARARGS},
    {"load", (PyCFunction)_load, METH_VARARGS},
    {NULL, NULL}
};


static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "cfbs",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_cfbs(void) {
    return PyModule_Create(&module);
};
