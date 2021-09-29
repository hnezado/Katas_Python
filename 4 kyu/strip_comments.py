# Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
# Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

def solution(string, markers):
	lines = string.split('\n')
	result = []
	for line in lines:
		has_markers = False
		for marker in markers:
			if marker in line:
				result.append(line[:line.find(marker)].strip())
				has_markers = True
				break
		if not has_markers:
			result.append(line)
	print('asdf', string, markers)
	return '\n'.join(result)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
