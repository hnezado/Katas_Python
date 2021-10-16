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
	if cleaned_tweet:
		if 'FIRE FIRE FIRE' in cleaned_tweet: cleaned_tweet = cleaned_tweet.replace('FIRE FIRE FIRE', 'You and you and you are fired!')
		cleaned_tweet = cleaned_tweet.replace('FIRE FIRE', 'You and you are fired!')
		cleaned_tweet = cleaned_tweet.replace('FIRE', 'You are fired!')
		cleaned_tweet = cleaned_tweet.replace('FURY FURY FURY', 'I am really really furious.')
		cleaned_tweet = cleaned_tweet.replace('FURY FURY', 'I am really furious.')
		cleaned_tweet = cleaned_tweet.replace('FURY', 'I am furious.')
		return cleaned_tweet
	else: return 'Fake tweet.'


print(fire_and_fury('FURYYYFIREYYFIRE'))
