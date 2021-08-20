# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.
#
# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


def is_isogram(string):
	return not any([1 if string.lower().count(c) > 1 else 0 for c in string.lower()])


print(is_isogram("Dermatoglyphics"))
# print(is_isogram("isogram"))
# print(is_isogram("aba"))
# print(is_isogram("moOse"))
# print(is_isogram("isIsogram"))
# print(is_isogram(""))
