#program to collect user details

correct = 'no'
#loop to allow user to re-enter if any details incorrect
while correct != 'yes':
    firstName = input('Enter first name: ')
    lastName = input('Enter lastname: ')
    telNum = input('Enter your phone number: ')
    #check phone number is correct length
    while len(telNum) != 11:
        print('Your phone number should be 11 digits long')
        telNum = input('Try again: ')
    print('Your details are:')
    print(firstName, lastName, 'phone number:', telNum)
    print('Are these details correct?')
    correct = input('Enter "yes" or "no": ')
print('Thanks for entering your details')
