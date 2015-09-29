import random


file = open('Normandy_exert.txt', 'r')

lines = file.readlines()
words = []
trigrams = {}
begining = "How shall"

for line in lines:
    words += line.split(' ')

for i in (range(len(words) - 2)):
    phrase = words[i] + " " + words[i + 1]
    if (phrase in trigrams):
        trigrams[phrase].append(words[i + 2])
    else:
        trigrams[phrase] = [words[i + 2]]


file.close()
