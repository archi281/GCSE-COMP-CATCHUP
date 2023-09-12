for i in range(0,4):
    def checkNumber():
        if num<50:
            print('Number is smaller than 50')
        elif num == 50:
            print('Number is 50')
        else:
            print('Number is bigger than 50')
            
    num = int(input("Enter a number: "))
    checkNumber()

print('Program over')
