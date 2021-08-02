# Create a function (or write a script in Shell)
# that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
	"""Returns even or odd depending of the given integer"""

	if number % 2 == 0:
		return 'Even'
	elif number % 2 != 0:
		return 'Odd'
