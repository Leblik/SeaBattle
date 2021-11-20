# Sea Battle Game
# Made by Leblik
#
# Beta version 0.3 of table game Sea Buttle.
#
# Поле игрока 1 и игрока 2 заданы изначально (10 x 10 клеток), пока что не меняются.
# В этой версии проверить механику выстрелов, отображения, записи и
# хранения резульатов выстрелов.

# IMPORTS
import random
# from print_fields_func import print_fields
# from xy_random_func import xy_random
# from print_fields_func import print_fields

print("\n  Sea Battle Game \n ver.0.3")
# Make fields of fleets for Player 1 and Computer.
# Ships in every fleet: x5 - 1, x4 - 1, x3 - 1, x2 - 2, x1 - 2

# STARTING DATA
# 1 var - by hand
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
fleet_comp = [[str(i) for i in row] for row in fleet_comp]

# Make fields of shots for Player 1 and Computer.
shots_pl_1 = [['~' for i in range(10)] for row in range(10)]
shots_comp = [['~' for i in range(10)] for row in range(10)]


# FUNCTIONS
# Function print_fields. Print 2 fields in one line
def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2):
    axis = list(range(1, 11))
    print("\nY   ", fleet_1_name, "field", " " * 17, fleet_2_name, "field")
    # print("v")
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        print(y, "   ", ' '.join([str(elem) for elem in ship_1]), " " * 12, y, "  ",
              ' '.join([str(elem) for elem in ship_2]))
    x_axis = ' '.join([str(x) for x in axis])
    print("    X", x_axis, " " * 16, x_axis)  # print x_axis
    # TODO: make print with format


# Function xy_random generate 2 number - coordinates in range(0,9)
def xy_random():
    randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
    return randomlist_2


# Function shots_func get shots from input coordinates Player or Computer
def shots_func(x, y, shots_field, target_fleet, name_who_turn, target_name):
    if shots_field[y][x] == '~':  # check repeat of coordinates Player shot
        if target_fleet[y][x] == '1':  # y1 - num of column, x1 - num of elem in string
            print(target_name + " ship is hit.")
            target_fleet[y][x] = 'X'
            shots_field[y][x] = 'X'
        elif target_fleet[y][x] == '0':
            print(name_who_turn + " miss... ")
            target_fleet[y][x] = '.'
            shots_field[y][x] = '.'
            # next Player(Computer) turn
    else:
        print("Повтор координат. Введите новые.")

print_fields("Player fleet", "Computer fleet", fleet_pl_1, fleet_comp)  # show players fleets
print_fields("Player shots", "Computer shots", shots_pl_1, shots_comp)  # show players shots

# GAME LOOP
# start values
run = True
turn_pl = True  # Player turns first
turn_comp = False  # Computer turns if Player miss

while run:

# Player turn
    while turn_pl:
        # shot player - input coordinates
        shot = input("\n Enter Player shot coordinate X Y to Computer:")

        if shot == 'n' or shot == 'q': # quit the game
            run = False
            print("\n", " " * 16, "Exit the game")
            exit()
        elif shot == '':  # debug cheat: if Player enter null string -> turn go to the Computer
            turn_pl = False
            turn_comp = True

        shot_pl_1 = [int(i) for i in shot.split()]
        x, y = shot_pl_1
        x, y = x - 1, y - 1  # correct coordinate from human to machine, coze list[0, 1, 2 ...]
        print("Player shot in x, y = ", x, "-", y)  # debug

        # shots_func(x, y, shots_pl_1, fleet_comp, "Player", "Computer")  # Player get shot

        if shots_pl_1[y][x] == '~':  # check repeat of coordinates Player shot
            # TODO: add turns counter for Player and Computer
            if fleet_comp[y][x] == '1':  # y - num of column, x - num of elem in string
                print("Computers ship is hit.")
                fleet_comp[y][x] = 'X'
                shots_pl_1[y][x] = 'X'
                # score_pl += 1
            elif fleet_comp[y][x] == '0':
                print("Player miss... Computer turn")
                fleet_comp[y][x] = '.'
                shots_pl_1[y][x] = '.'
                # next Player(Computer) turn
                turn_pl = False
                turn_comp = True
        else:
            print("Повтор координат. Введите новые.")

        print_fields("Player fleet", "Computer fleet", fleet_pl_1, fleet_comp)  # show players fleets
        print_fields("Player shots", "Computer shots", shots_pl_1, shots_comp)  # show players shots


# Computer turn
    while turn_comp:
        shot = input("\n May computer shots to of Player? Type anything for Yes or n/q - for Exit):")  # debug for Exit

        # quit the game
        if shot == 'n' or shot == 'q':
            run = False
            print("\n", " " * 16, "Exit the game")
            exit()


        # Generate random x & y coordinates for Computer shot
        x, y = xy_random()
        print("Computer shot in x, y = ", x + 1, y + 1)  # debug

        if shots_comp[y][x] == '~':  # check repeat of coordinates Computer shot
            if fleet_pl_1[y][x] == '1':  # y1 - num of column, x1 - num of elem in string
                print("Ship Player 1 is hit")
                fleet_pl_1[y][x] = 'X'
                shots_comp[y][x] = 'X'
            elif fleet_pl_1[y][x] == '0':
                print("Computer miss... Player turn")
                fleet_pl_1[y][x] = '.'
                shots_comp[y][x] = '.'
                # Player start his turn
                turn_pl = True
                turn_comp = False
        else:
            print("Повтор координат. Новый выстрел")

        print_fields("Player fleet", "Computer fleet", fleet_pl_1, fleet_comp)  # show players fleets
        print_fields("Player shots", "Computer shots", shots_pl_1, shots_comp)  # show players shots


# quit()
# exit()
