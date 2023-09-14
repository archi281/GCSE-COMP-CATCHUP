#Program to work out the total floor area of 3 rooms

#create function to work out the floor area of one room
def floorArea():
    roomLength = int(input('Enter the length of room: '))
    roomWidth = int(input('Enter width of room: '))
    area = roomLength * roomWidth
    print('Area of the room is', area)
    print

def main():
    print('Room 1')
    floorArea()
    print('Room 2')
    floorArea()
    print('Room 3')
    floorArea()

#call main program function
main()
