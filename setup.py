
# simplewrap - Simple wrapper for C libraries based on Ctypes 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 
# Feb 2015, Helsinki

# Use old Python build system, otherwise the extension libraries cannot be found. FIXME 
import sys
for arg in sys.argv: 
    if arg=="install":
        sys.argv.append('--old-and-unmanageable') 

from setuptools import setup, Extension
from glob import glob 

test_simplewrap_module = Extension('simplewrap.tests.test_simplewrap_c', ['simplewrap/tests/test_simplewrap_c.c']) 
test_matrices_module   = Extension('simplewrap.tests.test_matrices_c', ['simplewrap/tests/test_matrices_c.c']) 

setup(
    name='simplewrap',
    version='0.3.0',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['simplewrap', 'simplewrap.examples', 'simplewrap.tests'], 
    ext_modules=[test_simplewrap_module, test_matrices_module],
    test_suite = "simplewrap.tests", 
    url='http://www.occiput.io/',
    license='LICENSE.txt',
    description='Easy to use wrappers generator for C libraries based on ctypes.',
    long_description=open('README.rst').read(),
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "numpy >= 1.6.0", 
    ], 
)
