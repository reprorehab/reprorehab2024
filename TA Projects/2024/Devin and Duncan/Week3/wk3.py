# ReproRehab Pod 2 24/25 - Week 3 Activities 
# When you run this scipt you should see all tests fail, your goal is to edit 
# the code such that all tests pass 

import unittest 

class Week3(unittest.TestCase):

    def test_int(self):
        # Make x and integer 
        x = None # edit this line only
        self.assertTrue(type(x) is int)
    
    def test_str(self):
        # Make x a string
        x = None # edit this line only
        self.assertTrue(type(x) is str)

    def test_float(self):
        # Make x a float 
        x = None # edit this line only
        self.assertTrue(type(x) is float)

    def test_list(self):
        # Make x a list 
        x = None # edit this line only
        self.assertTrue(type(x) is list)

    def test_array(self):
        # Make x a numpy array 
        x = None # edit this line only
        self.assertTrue(type(x) is numpy.ndarray)

    def test_vector(self):
        # Make x a vector
        x = None # edit this line only
        self.assertTrue(type(x) is numpy.ndarray)
        self.assertTrue(len(numpy.shape(x)) == 1)
        self.assertTrue(numpy.shape(x)[0] >= 1)

    def test_scalar(self):
        # Make x a scalar
        x = None # edit this line only
        self.assertTrue(type(x) is numpy.ndarray)
        self.assertTrue(numpy.shape(x)[0] == 1)

    def test_tuple(self):
        # Make x a tuple 
        x = None # edit this line only
        self.assertTrue(type(x) is tuple)

    def test_bool(self):
        # Make x a bool 
        x = None # edit this line only
        self.assertTrue(type(x) is bool)

    def test_int2float(self):
        # Convert x from an int to float
        x_int = 1 
        self.assertTrue(type(x_int) is int)
        x_float = None # edit this line only (must use x_int variable)
        self.assertTrue(type(x_float) is float)

if __name__ == "__main__":
    unittest.main()

