# Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it,
# is to score a throw according to these rules. You will always be given an array with five six-sided dice values.
#
#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point
# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
# (contributing to the 500 points) or as a single 50 points, but not both in the same roll.
#
# Example scoring
#
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
# In some languages, it is possible to mutate the input to the function. This is something that you should never do.
# If you mutate the input, you will not be able to pass all the tests.

def score(dice):
    dices = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    points = 0
    for n in dice: dices[str(n)] += 1
    for dice_n, qty in dices.items():
        while dices[dice_n] >= 3:
            if dice_n == '1': points += 1000
            elif dice_n == '6': points += 600
            elif dice_n == '5': points += 500
            elif dice_n == '4': points += 400
            elif dice_n == '3': points += 300
            elif dice_n == '2': points += 200
            dices[dice_n] -= 3
        while dices[dice_n] > 0 and dice_n == '1':
            points += 100
            dices[dice_n] -= 1
        while dices[dice_n] > 0 and dice_n == '5':
            points += 50
            dices[dice_n] -= 1
    return points


print(score([5, 1, 3, 4, 1]))
print(score([1, 1, 1, 3, 1]))
print(score([2, 4, 4, 5, 4]))
