
# wrapid - Simple wrapper for C libraries based on Ctypes 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 


from setuptools import setup, Extension
from glob import glob 

test_wrapid_module = Extension('wrapid.tests.test_wrapid_c', ['wrapid/tests/test_wrapid_c.c']) 

setup(
    name='wrapid',
    version='0.1.0',
    author='Stefano Pedemonte',
    author_email='stefano.pedemonte@gmail.com',
    packages=['wrapid', 'wrapid.examples', 'wrapid.tests'], 
    ext_modules=[test_wrapid_module, ],
    test_suite = "wrapid.tests", 
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

