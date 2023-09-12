email1 = input('Enter your email address: ')
email2 = input('Confirm your email address: ')
while email1 != email2:
    print("That's either a different address or there's an error, try again")
    email1 = input('Enter your email address: ')
    email2 = input('Confirm your email address: ')
print('The email adresses match')
