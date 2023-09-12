question = input('Do you want to work out the area of a rectangle? Y or N         ')
count = 0
while question =='Y':
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    print('The area is ', width * height)
    question = input('Do you want to work out the area of a rectangle? Y or N            ')
    count = count + 1
print('You have chosen not to work out the area')
print('You have worked out the area for', count, 'rectangles in total')
