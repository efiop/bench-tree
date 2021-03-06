import os
import platform
import sys

from setuptools import setup, Extension

#if sys.version_info >= (3,) and platform.python_implementation() == 'CPython':
#    try:
#        import wheel.bdist_wheel
#    except ImportError:
#        cmdclass = {}
#    else:
#        class bdist_wheel(wheel.bdist_wheel.bdist_wheel):
#            def finalize_options(self):
#                self.py_limited_api = 'cp3{}'.format(sys.version_info[1])
#                super().finalize_options()
#
#        cmdclass = {'bdist_wheel': bdist_wheel}


setup(
    name='bench-tree',
    version='1.0.0',
    ext_modules=[
        Extension(
            'bench_tree.cfbs.cfbs',
            [os.path.join("bench_tree", "cfbs", "cfbs.c")],
#            py_limited_api=True,
#            define_macros=[('Py_LIMITED_API', None)],
        ),
    ],
#    cmdclass=cmdclass,
)
