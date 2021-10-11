# Your goal is to make a stack based programming language in Python with the following functions/tokens:
#
# start - Marks the start of the program.
# end - Marks the end of the program, and returns the top element in the stack.
# push x - Pushes the integer x into the stack.
# add - Adds together the top two elements on the stack.
# sub - Subtracts the top-most element by the second top-most element on the stack.
# mul - Multiplies the top two elements on the stack.
# div - Divides (integer division) the top-most element by the second top-most element on the stack.
# Demo:
#
#    start push 5 push 3 add end
#  = 8
#    start push 2 push 5 div push 3 push 8 mul mul end
#  = 48
# Easy, right?
#
# Such a trivial string interpreter is probably too simple for an amazing code warrior like you.
# To spice things up, we will add bubbles into the mix. Each token must be engulfed by a bubble (parentheses)!
#
# The syntax should be like:
#
# (start)(push)(4)(push)(9)(div)(end)
# which returns 2 in this case.
#
# Task
# Your goal is to create appropriate definitions for start, end, push, add, sub, mul and div
# so that the bubbly language is valid Python syntax, and evaluates to the correct value.
#
# For instance, typing this in a shell should result in:
#
# >>> (start)(push)(5)(push)(8)(push)(1)(add)(add)(end)
# 14
# See the example tests for more examples.
#
# Notes
# Your definitions should allow multiple bubbly language statements in one script (python session).
# Don't worry about division by 0. There won't be any test cases on that.
#
# All input will be valid.

start = lambda func: func([])
end = lambda a: a.pop()
push = lambda a: (lambda n: (lambda func: func(a + [n])))
add = lambda a: (lambda func: func(a + [a.pop() + a.pop()]))
sub = lambda a: (lambda func: func(a + [a.pop() - a.pop()]))
mul = lambda a: (lambda func: func(a + [a.pop() * a.pop()]))
div = lambda a: (lambda func: func(a + [a.pop() // a.pop()]))


print((start)(push)(5)(push)(8)(push)(1)(add)(add)(end))
