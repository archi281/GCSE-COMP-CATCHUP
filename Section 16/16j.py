#Program to convert between cm & m and m & cm

#create subroutine to turn m to cm
def mToCm():
    m = float(input('Enter number of metres: '))
    cm = m * 100
    print(m, 'm is', cm, 'cm')
def cmToM():
    cm = float(input('Enter number of centimetres: '))
    m = cm / 100
    print(cm, 'cm is', m, 'm')

def menu():
    print()
    print('Option menu - enter A, B or Q')
    print('A. Convert m to cm')
    print('B. Convert cm to m')
    print('Q. Quit the program')

#display options by calling menu subroutine then user chooses
menu()
conversion = input('Enter choice: ')
#loop to do conversions until user chooses to quit
while conversion != 'Q':
    if conversion == 'A':
        mToCm()
    elif conversation == 'B':
        cmToM()
    menu()
    conversation = input('Enter choice: ')
print('Program Ended')

