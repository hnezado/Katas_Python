# Digital root is the recursive sum of all the digits in a number.
#
# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# The input will be a non-negative integer.


def digital_root(n):
    """Calculates de sum of the given number digits"""

    str_num = str(n)

    if len(str_num) > 1:
        sum = 0
        for digit in str_num:
            sum += int(digit)

        return digital_root(sum)

    else:
        return n


print(digital_root(166))
