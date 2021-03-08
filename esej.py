
from random import randint
import string

def generate_word():
    length = randint(1,15)
    word = ""
    for i in range(length):
        word += string.ascii_lowercase[randint(0,25)]

    return word



lower_bound, upper_bound = map(int, input().split())

words = set()

num_words = max(lower_bound, upper_bound // 2 + 1)
while len(words) < num_words:
    words.add(generate_word())


print(' '.join(words))
