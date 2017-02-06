""" A function that generates prime numbers from 0 to n"""

def primenum(number):
	"""A function that generates prime numbers in n"""
	if not isinstance(number, int):
		raise TypeError