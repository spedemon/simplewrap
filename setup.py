
# simplewrap - Simple wrapper for C libraries based on Ctypes 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 


from setuptools import setup, Extension, Library
from glob import glob 

test_simplewrap_module = Library('simplewrap.tests.test_simplewrap_c', ['simplewrap/tests/test_simplewrap_c.c']) 
test_matrices_module   = Library('simplewrap.tests.test_matrices_c', ['simplewrap/tests/test_matrices_c.c']) 

setup(
    name='simplewrap',
    version='0.1.0',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['simplewrap', 'simplewrap.examples', 'simplewrap.tests'], 
    ext_modules=[test_simplewrap_module, test_matrices_module],
    test_suite = "simplewrap.tests", 
    url='http://niftyrec.scienceontheweb.com/',
    license='LICENSE.txt',
    description='Simple wrapper for C libraries based on ctypes.',
    long_description=open('README.txt').read(),
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    install_requires=[
        "numpy >= 1.7.1", 
    ], 
)

