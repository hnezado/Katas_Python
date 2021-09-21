# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:
#
#
# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

from functools import reduce


def snail(snail_map):
    snail_dict = dict.fromkeys(reduce(lambda x, y: x+y, snail_map), True)
    snail_nums = []
    # direction = 0
    lap = 0
    while lap < 1:
        snail_nums += snail_map[lap][lap:-1-lap]
        for row_index in range(len(snail_map)):
            snail_nums += [snail_map[row_index+lap][-1-lap]]

        print(1.2, snail_map[-1-lap][lap:len(snail_map[lap])+1])

        print(1.2, snail_map[-1-lap][0:3:-1])

        snail_nums += snail_map[-1-lap][-1-lap:lap+1:-1]
        for row_index in range(0, len(snail_map), -1):
            snail_nums += [snail_map[row_index+lap][lap]]
        lap += 1

        # if direction > 3: direction = 0
        # if not any(snail_dict.keys()): return snail_nums
    return snail_nums


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]))
