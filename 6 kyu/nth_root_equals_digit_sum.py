# There are numbers for which the n^th root equals the sum of their digits. For example:
#
# 3√512) = 5+1+2 = 8
#
# Complete the function that returns all natural numbers( in ascending order)
# for which the above statement is true for the given n, where 2 ≤ n ≤ 50
#
# Note To avoid hardcoding the answers, your code is limited to 1000 characters
#
# Examples
# 2-->  [1, 81]
# 3-->  [1, 512, 4913, 5832, 17576, 19683]

def nth_root_equals_digit_sum(n):
	result = list()
	for num in range(1, 1000):
		if sum([int(i) for i in str(num**n)]) == num:
			result.append(num**n)
	return result


print(nth_root_equals_digit_sum(3))
