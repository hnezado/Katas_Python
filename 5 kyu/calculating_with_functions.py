# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations:
# plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

num2 = ''


def zero(op=0):
	global num2
	if isinstance(op, int): num2 = 0
	else: return op(0)


def one(op=1):
	global num2
	if isinstance(op, int): num2 = 1
	else: return op(1)


def two(op=2):
	global num2
	if isinstance(op, int): num2 = 2
	else: return op(2)


def three(op=3):
	global num2
	if isinstance(op, int): num2 = 3
	else: return op(3)


def four(op=4):
	global num2
	if isinstance(op, int): num2 = 4
	else: return op(4)


def five(op=5):
	global num2
	if isinstance(op, int): num2 = 5
	else: return op(5)


def six(op=6):
	global num2
	if isinstance(op, int): num2 = 6
	else: return op(6)


def seven(op=7):
	global num2
	if isinstance(op, int): num2 = 7
	else: return op(7)


def eight(op=8):
	global num2
	if isinstance(op, int): num2 = 8
	else: return op(8)


def nine(op=9):
	global num2
	if isinstance(op, int): num2 = 9
	else: return op(9)


def plus(num1):
	return num1+num2 if type(num1) == int else plus


def minus(num1):
	return num1-num2 if type(num1) == int else minus


def times(num1):
	return num1*num2 if type(num1) == int else times


def divided_by(num1):
	return num1//num2 if type(num1) == int else divided_by


print(zero(times(two())))
