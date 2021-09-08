# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list
# of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array.
# If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum.
# Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
	max_sum = 0
	# max_seq = []
	for index in range(len(arr)):
		for length in range(1, len(arr[index:])+1):
			if sum(arr[index:index+length]) > max_sum:
				max_sum = sum(arr[index:index+length])
				# max_seq = arr[index:index+length]
	return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# print(max_sequence([]))
