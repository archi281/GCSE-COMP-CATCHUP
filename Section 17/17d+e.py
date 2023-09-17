def add2Ints():
    num1 = int(input('Enter 1st number to add up: '))
    num2 = int(input('Enter 2nd number to add up: '))
    addition = num1 + num2
    return addition
def main():
    print('This program will add up 2 integers')
    result = add2Ints()
    print('The answer is', result)
main()
