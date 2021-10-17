#include <Python.h>
#include <fcntl.h>
#include <sys/syscall.h>
#include <unistd.h>

#include "digest.h"

static PyObject*
_digest(PyObject* self, PyObject* args) {
    char* path1;
    char* path2;

    if (!PyArg_ParseTuple(args, "ss", &path1, &path2)) {
        return NULL;
    }

    if (syscall(SYS_renameat2, AT_FDCWD, path1, AT_FDCWD, path2, RENAME_EXCHANGE)) {
        return PyErr_SetFromErrno(PyExc_OSError);
    } else {
        Py_RETURN_NONE;
    }
}


static struct PyMethodDef methods[] = {
    {"digest", (PyCFunction)_digest, METH_VARARGS},
    {NULL, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "digest",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit_rename_exchange(void) {
    return PyModule_Create(&module);
};
