import random


n = random.randint(1,100)

count = 7

num = int(input('Please enter your guess: '))

while count > 0:

    if num == n:
        print('Yay, you win!!')
        print(f'You guessed it in {7 - count} attempts.')
        break

    count -= 1

    print('Wrong!')

    if num > n:
        print('Your guess is too high.')
    elif num < n:
        print('Your guess is too low.')

    if count > 0:
        print(f'Only {count} attempts left.')
        num = int(input('Please enter another guess: '))

    else:
        print('You lose!')
        print(f'The answer was {n}.')