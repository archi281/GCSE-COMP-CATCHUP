#Program to work out area of triangle or square
#create subroutine to work out area of a triangle
def areaTriangle():
    base = int(input('Enter base: '))
    height = int(input('Enter height: '))
    area = 0.5 * base * height
    print('Area of triangle is', area)
#create subroutine to work out area of a square
def areaSquare():
    side = int(input('Enter length of side: '))
    area = side * side
    print('Area of square is', area)
#create subroutine to work out area of a rectangle
def areaRectangle():
    width = int(input('Enter the length of the width: '))
    height = int(input('Enter the length of the height: '))
    print('Area of a rectangle is', height * width)
#user chooses which area to work out
print('Enter T for area of triangle')
print('Enter S for area of square')
print('Enter R for rectangle')
shape = input('Enter T, R or S: ')
if shape == 'T':
    areaTriangle()
elif shape == 'S':
    areaSquare()
elif shape == 'R':
    areaRectangle()
