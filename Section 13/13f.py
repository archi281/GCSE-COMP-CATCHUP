import random
print('I am going to roll a die.')
print('Guess what number that I will roll')
die = random.randint(1,6)
guess = int(input('Enter a number from 1 - 6: '))
if guess == die:
    print('You win, the number was', die)
else:
    print('You lost, the number was', die)
