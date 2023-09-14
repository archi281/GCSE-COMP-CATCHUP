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
def mToKm():
    m = float(input('Enter the number of metres:'))
    km = m / 1000
    print(m, 'm is', km, 'km')
def kmToM():
    km = float(input('Enter the number of metres:'))
    m = km * 1000
    print(km, 'km is', m, 'm')
def menu():
    print()
    print('Option menu - enter A, B, C, D or Q')
    print('A. Convert m to cm')
    print('B. Convert cm to m')
    print('C. Convert m to km')
    print('D. Convert km to m')
    print('Q. Quit the program')

#display options by calling menu subroutine then user chooses
menu()
conversion = input('Enter choice: ')
#loop to do conversions until user chooses to quit
while conversion != 'Q':
    if conversion == 'A':
        mToCm()
    elif conversion == 'B':
        cmToM()
    elif conversion == 'C':
        mToKm()
    else:
        kmToM()
    menu()
    conversion = input('Enter choice: ')
print('Program Ended')

