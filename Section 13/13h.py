import random
print('Mr Teachalot has bought some bule and purple pens')
print('There is a 1 in 3 chance of getting a purple pen')
print('Press enter to see what colur you will be using')
input()
chance = random.randint(1, 3)
if chance == 1:
    print('You get a purple pen')
else:
    print('You get a blue pen')
    
