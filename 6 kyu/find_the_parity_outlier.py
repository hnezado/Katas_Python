# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

def find_outlier(integers):
    even_qty = len([i for i in integers if i % 2 == 0])
    odd_qty = len([i for i in integers if i % 2 != 0])
    return list((filter(lambda x: x % 2 != 0, integers)) if even_qty > odd_qty else (filter(lambda x: x % 2 == 0, integers)))[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
