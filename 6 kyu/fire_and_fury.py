# The President's phone is broken
# He is not very happy.
#
# The only letters still working are uppercase E, F, I, R, U, Y.
#
# An angry tweet is sent to the department responsible for presidential phone maintenance.
#
# Kata Task
# Decipher the tweet by looking for words with known meanings.
#
# FIRE = "You are fired!"
# FURY = "I am furious."
# If no known words are found, or unexpected letters are encountered, then it must be a "Fake tweet."
#
# Notes
# The tweet reads left-to-right.
# Any letters not spelling words FIRE or FURY are just ignored
# If multiple of the same words are found in a row then plural rules apply -
# FIRE x 1 = "You are fired!"
# FIRE x 2 = "You and you are fired!"
# FIRE x 3 = "You and you and you are fired!"
# etc...
# FURY x 1 = "I am furious."
# FURY x 2 = "I am really furious."
# FURY x 3 = "I am really really furious."
# etc...
# Examples
# ex1. FURYYYFIREYYFIRE = "I am furious. You and you are fired!"
# ex2. FIREYYFURYYFURYYFURRYFIRE = "You are fired! I am really furious. You are fired!"
# ex3. FYRYFIRUFIRUFURE = "Fake tweet."

def fire_and_fury(tweet):
	cleaned_tweet = ''
	for ind, c in enumerate(tweet):
		if c not in 'EFIRUY': return 'Fake tweet.'
		else:
			if tweet[ind:ind+4] in ['FURY', 'FIRE']: cleaned_tweet += tweet[ind:ind+4]+' '
	cleaned_tweet = cleaned_tweet.strip()

	word_count = list()
	for w in cleaned_tweet.split():
		if len(word_count) == 0: word_count.append([w, 1])
		else:
			if word_count[-1][0] == w: word_count[-1][1] += 1
			else: word_count.append([w, 1])
	result_tweet = ''.join([f'I am {"really "*(w[1]-1)}furious. ' if w[0] == 'FURY' else f'You {"and you "*(w[1]-1)}are fired! ' for w in word_count]).strip()
	return result_tweet if result_tweet else 'Fake tweet.'


print(fire_and_fury('FURYYYFURYFIREFURYFIREYYFIRE'))
