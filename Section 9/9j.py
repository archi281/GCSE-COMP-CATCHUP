def rectangle():
    width = int(input('Enter the width of the rectangle: '))
    height = int(input('Enter the length of the rectangle: '))
    print('The area of the rectangle is ', width * height)

def triangle():
    base = int(input('Enter the length of the base of your triangle: '))
    height = int(input('Enter the height of your triangle; '))
    print('The area of your triangle is', base * height * 0.5)

choice = input('Do you want to work out the area of a rectangle of a triangle? (no caps lock please)        ')
while choice not in ('rectangle', 'triangle'):
    print('Please enter rectangle or triangle')
    choice = input('Do you want to work out the area of a rectangle of a triangle? (no caps lock please)        ')
if choice == 'rectangle':
    rectangle()
elif choice == 'triangle':
    triangle()

