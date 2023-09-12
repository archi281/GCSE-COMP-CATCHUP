amount = int(input('Enter the amount thay you offer for the coat: '))
while amount < 25:
    print('Too low, enter a higher number')
    amount = int(input())
print('Sold! The coat is yours!')
