# A comfortable word is a word which you can type always alternating the hand you type with
# (assuming you type using a QWERTY keyboard and use fingers as shown in the image below).
#
# That being said, create a function which receives a word and returns true/True
# if it's a comfortable word and false/False otherwise.
#
# The word will always be a string consisting of only ascii letters from a to z.
#
# To avoid problems with image availability, here's the lists of letters for each hand:
#
# Left: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
# Right: y, u, i, o, p, h, j, k, l, n, m


def comfortable_word(word):
  left_letters = 'qwertasdfgzxcvb'
  right_letters = 'yuiophjklnm'
  hand = ''
  for c in word:
    if c in left_letters:
      if hand == 'left': return False
      else: hand = 'left'
    elif c in right_letters:
      if hand == 'right': return False
      else: hand = 'right'
  return True


print(comfortable_word('yams'))
print(comfortable_word('test'))
