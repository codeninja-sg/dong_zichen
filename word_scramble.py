from random import shuffle
#input()
#print()
word_list = [
    "python",
    "games",
    "code",
    "fun",
    "list",
]

def scramble_word(word):
    letter_list = list(word)
    shuffle(letter_list)
    scramble = "".join(letter_list)
    return scramble

