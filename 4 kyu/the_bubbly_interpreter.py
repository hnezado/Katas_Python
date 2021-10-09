# This kata is a harder version of A Bubbly Programming Language. If you haven't done that,
# I would suggest doing it first.
#
# You are going to make yet another interpreter similar to A Bubbly Programming Language,
# but with completely different syntax.
#
# Your goal is to create an interpreter for a programming language (bubbly language) with the following tokens:
#
# start: marks the start of a program
# return_ (return_ <value>): marks the end of a program, and returns the given <value>
# let (let <var_name> <value>): sets the variable <var_name> to the given <value>
# add (add <value> <value>) returns the sum of the two <value>
# sub (sub <value> <value>) returns the result of the first <value> minus the second <value>
# mul (mul <value> <value>) returns the product of the two <value>
# div (div <value> <value>) returns the result of the first <value> divided by the second <value> (integer division)
# Each <value> can either be an integer (immediate value), a string (value of the variable), or an operator
# (add, sub, etc) (return value of the operator).
#
# An example code in the bubbly language (but without the bubbles) looks like:
#
# start
# let 'my_var' add 5 8
# let 'banana' mul 'my_var' 2
# return_ 'banana'
# and is equivalent to this pseudo code:
#
# let my_var = 5 + 8
# let banana = my_var * 2
# return banana
# and should return 26.
#
# Just like the easier counterpart of this kata, each token must be engulfed by a bubble (parenthesis)!
#
# So the above code should look like:
#
# (start)(let)('my_var')(add)(5)(8)(let)('banana')(mul)('my_var')(2)(return_)('banana')
# and returns 26.
#
# Your goal is to create appropiate definitions for start, let, return_, add, sub, mul, div
# so that the bubbly language is valid Python syntax.
#
# More examples:
#
# >>> (start)(let)('x')(20)(return_)(sub)(10)('x')
# -10
#
# >>> (start)(return_)(mul)(10)(15)
# 150
# Extra Requirements
# Custom classes are not allowed in the solution, as Python's __call__ overloading makes this problem too trivial.
# Your solution must use functions and lambdas to achieve this instead
# (the class and type keywords are banned! Muhahahahahaha!).
#
# In addition, your interpreter should allow nested operators. Since each operator takes in exactly 2 parameters,
# it is possible to deduce the hierarchy of the nested structure.
#
# This:
#
# add add 5 add 3 2 5
# has this structure:
#
# add(add(5, add(3, 2)), 5)
# And therefore this should be valid syntax:
#
# >>> (start)(return_)(add)(add)(5)(add)(3)(2)(5)
# 15
# Lastly, there will be partial code.
#
# >>> f = (start)(let)('a')(20)(return_)(add)('a')
# >>> (f)(10)
# 30
# >>> (f)(5)
# 25
# Notes
# There will be no indication of line-breaks (or end of statement) in bubbly language.
# You will need to deduce that from the tokens yourself.
#
# You may assume that all inputs are valid.
#
# eval and exec are also not allowed.

# remember: custom classes are NOT allowed!

start = None
return_ = None
let = None
add = None
sub = None
mul = None
div = None