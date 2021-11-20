import random


# Function xy_random generate 2 number - coordinates in range(0,9)
def xy_random():
    randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
    # randomlist_2 = [i*random.randint(0, 9) for i in range(2)]
    return randomlist_2

# Example:
# print(xy_random())
