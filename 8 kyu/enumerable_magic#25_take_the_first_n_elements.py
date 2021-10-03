# Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements
# from the list/array.
#
# If you need help, here's a reference:
#
# https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range


def take(arr, n):
    return [num for index, num in enumerate(arr) if index in range(n)]


print(take([0, 1, 2, 3, 5, 8, 13], 3))
