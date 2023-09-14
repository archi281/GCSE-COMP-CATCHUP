import random
amount = int(input('Enter the amount of times thtat you want to roll the die: '))
for count in range(amount):
    die = random.randint(1,6)
    print('You have rolled: ', die)
