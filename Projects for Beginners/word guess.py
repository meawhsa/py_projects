import random
import re

words = [
    'rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks'
]

def find_index(st,lt):
    matches = []
    for i, c in enumerate(st):
      if c == lt:
        matches.append(i)
    return matches

word = random.choice(words)
guess = ['_'] * len(word)

count = 12
while count >0 :
    if '_' not in guess :
        print('you win')
        print(f'word is {word}')
        break
    
    print(' '.join(guess))
    count -= 1
    letter = input('enter ')
    if letter in word:
        indexs = find_index(word,letter)
        for i in indexs:
           guess[i] = letter
    

    if count == 0 :
        print('you loose') 
        print(f'answer is {word}')
