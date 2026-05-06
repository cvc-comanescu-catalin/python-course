# Creating tuples (use parentheses)
point = (3, 7)
rgb = (255, 128, 0)
single = (42,)   # <- Note the comma! (42) is just an int
 
# Accessing elements — same as lists
print(point[0])   # 3
print(rgb[-1])    # 0
 
# Unpacking
x, y = point
print(f"x={x}, y={y}")   # x=3, y=7
 
lat, lon = 44.4268, 26.1025   # Bucharest coordinates


def get_treasure_location():
    ''' 
    Get the location of the treasure
    returns a tuple:
    [0] is a string naming the landmark to start
    [1] is the number of paces north
    [2] is the number of paces east
    '''
    # get the location from the pirate
    return ('The old oak tree', 20, 30)

location = get_treasure_location()
print ('Start at', location[0], 'walk', location[1], 'paces north', 'and', location[2], 'paces east. ')