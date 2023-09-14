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
#user chooses which area to work out
print('Enter T for area of triangle')
print('Enter S for area of square')
shape = input('Enter T or S: ')
if shape == 'T':
    areaTriangle()
elif shape == 'S':
    areaSquare()
