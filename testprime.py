"""A collection of test cases that checks if the program is working well"""
import unittest
from prime import primenum

class TestPrime(unittest.TestCase):
    """A class that contains testcases of primenumbers"""
    def test_if_it_accepts_string_datatype(self):
        """Tests if string datatype is accepted"""
        with self.assertRaises(TypeError):
            primenum("string")

    def test_if_it_accepts_dictionary(self):
        """Test if dictionary datatype is accepted"""
        with self.assertRaises(TypeError):
            primenum("{}")

    def test_if_it_accepts_lists(self):
        """Test if list datatype is accepted"""
        with self.assertRaises(TypeError):
            primenum("[]")







    
    



