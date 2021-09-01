# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(array):
    result = list(filter(lambda x: x != 0, array))
    for _ in range(array.count(0)): result.append(0)
    return result


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
