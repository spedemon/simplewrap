
# SimpleWrap - Simple wrapper for C libraries based on ctypes 
# Stefano Pedemonte
# Aalto University, School of Science, Helsinki
# Oct 2013, Helsinki 

__all__ = ['echo']

from .. import c_python
import unittest
import os
import random

class TestSimpleWrap(unittest.TestCase): 
    """Sequence of tests for SimpleWrap. """   
    def setUp(self):
        # Load library
        self.lib = c_python.load_c_library("test_simplewrap_c",os.path.split(__file__)[0])

    def test_int(self):
        """Wrap a simple function with integer parameters. """
        number = random.randint(1,1e6)
        descriptor = [  {'name':'input',  'type':'int', 'value':number},
                        {'name':'output', 'type':'int', 'value':None },  ]
        r = c_python.call_c_function( self.lib.echo, descriptor ) 
        self.assertTrue(r.output == number)

    def test_numpy_array(self):
        """Wrap a simple function with numpy ndarray parameters. """
        pass

    def test_string(self):
        """Wrap a simple function with string parameter. """
        pass


if __name__ == '__main__':
    unittest.main()