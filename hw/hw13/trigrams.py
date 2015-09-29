import random

import string

file = open('Normandy_exert.txt', 'r')

lines = file.readlines()
words = []
trigrams = {}

for line in lines:
    words += line.split(' ')

for i, word in enumerate(words):
    if (i < len(words) - 2):
        trigrams[(word, words[i + 1])] = words[i + 2]


print(str(words))
print(str(trigrams))

'''for i in (range(len(words) - 2)):
   phrase = words[i] + " " + words[i + 1]
   if (phrase in trigrams):
       trigrams[phrase].append(words[i + 2])
   else:
       trigrams[phrase] = [words[i + 2]]'''
