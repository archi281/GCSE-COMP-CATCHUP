import random
print('I am going to toss a coin.')
print('Guess whether it will be heads or tails showing')
coin = random.randint(1,2)
if coin == 1:
    coinSide = 'heads'
else:
    coinSide = 'tails'
guess = input('Enter "heads" or "tails": ')
if guess == coinSide:
    print("You win, it landed", coinSide)
else:
    print("You lost, it landed", coinSide)
