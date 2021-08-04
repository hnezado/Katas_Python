# Write a function that takes in a string of one or more words,
# and returns the same string, but with all five or more letter words reversed (like the name of this kata).
#
# Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

def spin_words(sentence):
    words = sentence.split(' ')
    result = ''
    for word in words:
        checked_word = ''
        if len(word) >= 5:
            for n in range(len(word)):
                letter_index = len(word)-n-1
                checked_word += word[letter_index]
        else:
            checked_word += word

        result += checked_word + ' '
    result = result[:-1:]
    return result

