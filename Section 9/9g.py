question = input('Do you want to work out the area of a rectangle? Y or N         ')
while question =='Y':
    width = int(input('Enter width: '))
    height = int(input('Enter height: '))
    print('The area is ', width * height)
    question = input('Do you want to work out the area of a rectangle? Y or N            ')
print('You have chosen not to work out the area')
