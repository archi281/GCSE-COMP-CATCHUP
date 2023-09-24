calc = 2 + 4
print('What is 2 + 4? ')
ans = int(input())

while ans != calc:
    print('Wrong, try again')
    ans = int(input())

print('Well Done')
print('2 + 4 =', calc)
