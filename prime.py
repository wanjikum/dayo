""" A function that generates prime numbers from 0 to n"""

def primenum(number):
	"""A function that generates prime numbers in n"""
	if not isinstance(number, int):
		raise TypeError

	if number <= 0:
		return "Numbers less than or equal to zero are not allowed!"

	elif number == 1:
		return "One is not considered prime number"
		