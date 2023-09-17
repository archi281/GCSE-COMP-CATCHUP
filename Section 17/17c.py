#create function to work out floor area of a room
def floorArea():
    sideA = int(input('Enter length of room side A: '))
    sideB = int(input('Enter length of room side B: '))
    area = sideA * sideB
    return area
#create main program function
def main():
    #work out area of 1st room by calling floorArea() function
    areaRoom1 = floorArea()
    print('Area of room 1 is', areaRoom1)
    #work out area of 2nd room by calling floorArea() function
    areaRoom2 = floorArea()
    print('Area of room 2 is', areaRoom2)
    #work out area of 3rd room by calling floorArea() function
    areaRoom3 = floorArea()
    print('Area of room 3 is', areaRoom3)
    #work out total area of all 3 rooms
    total = areaRoom1 + areaRoom2 + areaRoom3
    print('Total area of 3 rooms is', total)
#call main program function
main()
