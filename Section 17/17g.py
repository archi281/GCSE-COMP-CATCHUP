def rectangleArea():
    length = int(input('Enter the length of the rectangle: '))
    width = int(input('Enter the width of the rectangle: '))
    return length * width

def triangleArea():
    base = int(input('Enter the length of the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))
    area = base * height * 0.5
    return area

def main():

     triangleArea()
     rectangleArea()


main()

