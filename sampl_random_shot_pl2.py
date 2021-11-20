# import random

# Make fields of fleets for player 1 and player 2.
# Ships in every fleet: x5 - 1, x4 - 1, x3 - 1, x2 - 2, x1 - 2
# 1 var - by hand
from xy_random_func import xy_random

fleet_pl_1 = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
              [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]

fleet_comp = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
              [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
              [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Change int elmnts to str in fleets
fleet_pl_1 = [[str(i) for i in row] for row in fleet_pl_1]
fleet_comp = [[str(i) for i in row] for row in fleet_pl_1]

# Make fields of shots for player 1 and player 2.
shots_pl_1 = [['~' for i in range(10)] for row in range(10)]
shots_comp = [['~' for i in range(10)] for row in range(10)]

# Function print_fields. Print 2 fields in one line
def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2):
    axis = list(range(1, 11))
    print("\nY   ",fleet_1_name,"field", " " * 17, fleet_2_name, "field")
    # print("v")
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        print(y, "   ", ' '.join([str(elem) for elem in ship_1]), " " * 12, y,"  ", ' '.join([str(elem) for elem in ship_2]))
    x_axis = ' '.join([str(x) for x in axis])
    print("    X", x_axis, " " * 16, x_axis)   # print x_axis


# Function xy_random generate 2 number - coordinates in range(0,9)
# def xy_random():
#     randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
#     return randomlist_2


# Game loop
run = True
while run:
    # print_fields("Player 1 fleet", "Computer fleet", fleet_pl_1, fleet_comp)    # show players fleets
    print_fields("Player 1 fleet", "Computer shots", fleet_pl_1, shots_comp)    # show Player 1 fleet and Computer shots

# Player 2 / Computer make shot
    shot = input("\n May computer shots to of Player? Type anything for Yes or n/q - for Exit):")  # debug

# quit the game
    if shot == 'n' or shot == 'q':
        run = False
        print("\n", " " * 16, "Exit the game")
        exit()

    # Generate random x & y coordinates for shot Player 2 / Computer
    x2, y2 = xy_random()
    print("Computer shot in x2, y2 = ", x2+1, y2+1)  # debug

    if shots_comp[y2][x2] == '~':  # check repeat of coordinates Computer shot
        if fleet_pl_1[y2][x2] == '1':  # y1 - num of column, x1 - num of elem in string
            print("Ship Player 1 is hit")
            fleet_pl_1[y2][x2] = 'X'
            shots_comp[y2][x2] = 'X'
        elif fleet_pl_1[y2][x2] == '0':
            print("Computer miss... Player 1 lets shot ")
            fleet_pl_1[y2][x2] = '.'
            shots_comp[y2][x2] = '.'
            # Player start his turn
    # else:
    #     x2, y2 = xy_random()  # for Computer, or input x y for Player1


# gdg
