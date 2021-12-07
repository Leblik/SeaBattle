# Sea Battle Game
# Made by Leblik
#
# Beta version 0.4 of table game Sea Buttle.
#
# Поле игрока 1 и игрока 2 заданы изначально (10 x 10 клеток), пока что не меняются.
# В этой версии проверить механику выстрелов, отображения, записи и
# хранения резульатов выстрелов.

# IMPORTS
# import sys
# import random
from all_func import print_fields
from all_func import xy_random
from all_func import shots_func

print("\n  Sea Battle Game \n ver.0.3"
      "\nTo make shot input coordinates of Computer fleet (X Y), range from 1 to 10, and then tap Enter."
      "\nFor exit input 'q' or 'n'.")
# Make fields of fleets for Player 1 and Computer.
# Ships in every fleet: x5 - 1, x4 - 1, x3 - 1, x2 - 2, x1 - 2

# STARTING DATA
# 1 var - by handmade fields
fleet_pl = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
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
fleet_pl = [[str(i) for i in row] for row in fleet_pl]
fleet_comp = [[str(i) for i in row] for row in fleet_comp]

# Make fields of shots for Player 1 and Computer.
shots_pl_1 = [['~' for i in range(10)] for row in range(10)]
shots_comp = [['~' for i in range(10)] for row in range(10)]


# FUNCTIONS
# Function print_fields. Print 2 fields in one line
# def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2):
#     axis = list(range(1, 11))
#     print("\nY      ", fleet_1_name, "fleet", " " * 25, fleet_2_name, "fleet")
#     # print("v")
#     for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
#         print(y, "   ", ' '.join([str(elem) for elem in ship_1]), " " * 12, y, "  ",
#               ' '.join([str(elem) for elem in ship_2]))
#     x_axis = ' '.join([str(x) for x in axis])
#     print("    X", x_axis, " " * 16, x_axis)  # print x_axis
#     print("       ", fleet_1_name + " score:", score_count_1, " "*23 + fleet_2_name + " score:", score_count_2)
#     print("-" * 70)
#     # TODO: make print with format
#
#
# # Function xy_random return list of 2 various random number (range(0,9)) - coordinates x,y
# def xy_random():
#     randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
#     return randomlist_2
#
#
# # Function shots_func get shots from input coordinates Player or Computer
# def shots_func(x, y, shots_field, fleet_target, name_who_turn, name_target, turn_count, score_count, turn_shoter):
#     if shots_field[y][x] == '~':  # check repeat of coordinates Player shot
#         playsound(sys.path[1] + '\\sound\\rocket_1.mp3')  # playing rocket sound
#         turn_count += 1  # counter of turns +1
#         print(name_who_turn + " turns:", turn_count)  # debug
#         if fleet_target[y][x] == '1':  # y - num of column, x - num of elem in string
#             playsound(sys.path[1] + '\\sound\\bang_3s.mp3')  # playing rocket bang sound
#             print(name_target + " ship is hit.")
#             fleet_target[y][x] = '\x1b[1;31;48m' + 'X' + '\x1b[0m'  # colored X
#             shots_field[y][x] = '\x1b[1;31;48m' + 'X' + '\x1b[0m'  # colored X
#             score_count += 1  # player score counter +1
#             turn_shoter = True
#         elif fleet_target[y][x] == '0':
#             playsound(sys.path[1] + '\\sound\\plop_1s.mp3')  # playing miss plop sound
#             print("\n", name_who_turn + " miss... ")
#             fleet_target[y][x] = '\x1b[1;34;48m' + 'o' + '\x1b[0m'  # colored o
#             shots_field[y][x] = '\x1b[1;34;48m' + 'o' + '\x1b[0m'  # colored o
#             turn_shoter = False  # next Player(Computer) turn
#     else:
#         print("Повтор координат. Введите новые.")
#     print("debug in shot_func:", turn_shoter, turn_count, score_count)  # debug
#     return [turn_shoter, turn_count, score_count]  # return turn_pl/comp flag , turn counter and score counter

# Function gameover check scores and return flag end of game
def gameover(score_pl, score_comp):
    if score_pl == 18:
        print("You WIN!")
        # return False
        exit()
        return False
    elif score_comp == 18:
        print("         GAME OVER \n      Computer WIN!")
        exit()
        return False
    else:
        return True



# GAME LOOP
# start values
run = True
turn_pl = True  # Player turns first
turn_comp = False  # Computer turns if Player miss
# add turns counters for Player and Computer
num_turn_pl = 0
num_turn_comp = 0
# add score counters - GAMEOVER condition
score_pl = 0
score_comp = 0

print_fields("Player", "Computer", fleet_pl, shots_pl_1, score_pl, score_comp)  # show Players fleet and shots fields


while run:

# Player turn
    while turn_pl and run:
        # shot player - input coordinates
        shot = input("\n Enter coordinate X Y (1-10) to make shot:")

        if shot == 'n' or shot == 'q': # quit the game
            print("\n", " " * 16, "Exit the game")
            turn_pl = False
            run = False
            # exit()
            break
        elif shot == '':  # debug cheat: if Player enter null string -> turn go to the Computer
            turn_pl = False
            turn_comp = True
        elif shot == 'win':  # debug cheat: if Player enter 'win' -> Player WIN! GAMEOVER
            score_pl = 18
            # turn_pl = False
            # turn_comp = False
            # run = False
            # break
            # exit()
        else:
            xy_pl = [int(i) for i in shot.split()]
            x, y = xy_pl
            x, y = x - 1, y - 1  # correct coordinate from human to machine, coze list[0, 1, 2 ...]

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func
        # turn_pl, run = gameover(score_pl, score_comp)  # check scores for GAMEOVER
        if turn_pl == False and run == True:
            turn_comp = True

        # turn_pl =  gameover(score_pl, score_comp)  # check scores for GAMEOVER
        # print("Player shot in x, y = ", x, "-", y)  # debug

        # Player get shot
        player_shot = shots_func(x, y, shots_pl_1, fleet_comp, "Player", "Computer", num_turn_pl, score_pl, turn_pl)
        print(x, y, "Player -> Computer", player_shot)  # debug
        turn_pl, num_turn_pl, score_pl = player_shot  # return result of shot



        print_fields("Player", "Computer", fleet_pl, shots_pl_1, score_pl, score_comp)  # show Players fleet and shots fields


# GAMEOVER - Player WIN # TODO: +make function GAMEOVER
        # if score_pl == 18:
        #     print("You WIN!")
        #     run = False
        #     exit()

        # run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func
        # # turn_pl, run = gameover(score_pl, score_comp)  # check scores for GAMEOVER
        if turn_pl == False and run == True:
            turn_comp = True


# Computer turn
    while turn_comp:

        # Generate random x & y coordinates for Computer shot
        x, y = xy_random()
        # print("\n Computer shot in x y = ", x + 1, y + 1)  # debug

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER  TODO: +make function GAMEOVER

        comp_shot = shots_func(x, y, shots_comp, fleet_pl, "Computer", "Player", num_turn_comp, score_comp,
                               turn_comp)  # Computer get shot
        print(x, y, "Player -> Computer", comp_shot)  # debug
        turn_comp, num_turn_comp, score_comp = comp_shot

        print_fields("Player", "Computer", fleet_pl, shots_pl_1, score_pl, score_comp)  # show Players fleet and shots fields

        # if turn_comp == False:
        #     turn_pl = True

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER TODO: +make function GAMEOVER

        # GAMEOVER - Computer WIN
        # if score_comp == 18:
        #     print("         GAME OVER \n      Computer WIN!")
        #     run = False
        #     exit()
        if turn_comp == False and run == True:
            turn_pl = True
# quit()
exit()
