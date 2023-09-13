import random
print('Use this program to practice addition.')
print('How many questions do you want to try?')
repeat = int(input())
while repeat > 0:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    total = num1 + num2
    print(num1, '+', num2, '= ')
    answer = int(input())
    if answer ==  total:
        print('Correct, well done')
    else:
        print('Wrong, asnwer is', total)
    repeat = repeat - 1
print('Practice is over')
