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
            primenum({})

    def test_if_it_accepts_lists(self):
        """Test if list datatype is accepted"""
        with self.assertRaises(TypeError):
            primenum([])

    def test_if_it_accepts_lists(self):
        """Test if list datatype is accepted"""
        with self.assertRaises(TypeError):
            primenum(56.58)

    def test_if_input_is_negative(self):
    	"""Tests if it accepts negative numbers"""
    	self.assertEquals(primenum(-5), "Numbers less than or equal to zero are not allowed!")

    def test_if_input_is_one(self):
    	"""Tests if one is a prime number"""
    	self.assertEquals(primenum(1), "One is not considered prime number")

    def test_if_input_is_zero(self):
    	"""Tests if zero is a prime number"""
    	self.assertEquals(primenum(0), "Numbers less than or equal to zero are not allowed!")

    def test_if_it_outputs_correct_output(self):
    	"""Tests if it outputs correct result"""
    	self.assertEquals(primenum(5), [2, 3, 5])

    def test_if_it_outputs_correct_output_for_numbers_greater_than_50(self):
    	"""Tests if it outputs correct result"""
    	self.assertEquals(len(primenum(55)), 16)

    def test_if_it_includes_a_number_i(self):
    	"""Tests if a number is prime is included in the list"""
    	self.assertIn(5, primenum(5))

    def test_if_it_includes_a_number_if_the_number_is(self):
    	"""Tests the input number is prime is included in the list"""
    	self.assertNotIn(16, primenum(16))


  



    











    
    



