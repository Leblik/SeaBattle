# Sea Battle Game
# Made by Leblik
#
# Beta version 0.5 of table game Sea Buttle.
#
# Поле игрока 1 и игрока 2 заданы изначально (10 x 10 клеток), пока что не меняются.
# В этой версии проверить механику выстрелов, отображения, записи и
# хранения резульатов выстрелов.

# IMPORTS
# import sys
# import random
# from all_func import print_fields, xy_random, shots_func, gameover
from all_func import *

print("\n  Sea Battle Game \n ver.0.5"
      "\nTo make a shot input coordinates of Computer fleet (X Y), range from 1 to 10, and then tap Enter."
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
shots_pl = [[Fore.BLUE + '~' + Fore.RESET for i in range(10)] for row in range(10)]  # add colored of field
shots_comp = [[Fore.BLUE + '~' + Fore.RESET for i in range(10)] for row in range(10)]  # add colored of field

# change elements in Computer shots field "shots_comp":  [~ ~ ~ ~] -> [A A ~ ~]
for i in range(10):
    for j in range(10):
        if fleet_pl[i][j] == "1":
            shots_comp[i][j] = Fore.GREEN + 'A' + Fore.RESET


# start values
run = True
turn_pl = True  # Player turns first
turn_comp = False  # Computer turns if Player miss
# input_player_flag = True
player_shot_flag = False
# add turns counters for Player and Computer
num_turn_pl = 0
num_turn_comp = 0
# add score counters - GAMEOVER condition
score_pl = 0
score_comp = 0
# add story lists of player and computer shots
shots_story_pl = []
shots_story_comp = []

# show Players fleet and shots fields
print_fields_2("Player", "Computer", shots_comp, shots_pl, score_pl, score_comp, num_turn_pl, num_turn_comp)

# GAME LOOP
while run:

    # Player turn LOOP
    while turn_pl and run:
        # player_shot_flag = False
        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func

        player_shot_flag = False

        # Player input coordinates LOOP
        # with ERROR check
        while True:
            # input string of coordinates X Y
            shot_str = input("\n Enter coordinate X & Y (1-10) to make shot:")

            try:
                if shot_str == 'n' or shot_str == 'q':  # Exit/quit the game code
                    # print(shot_str)  # debug
                    print("\n", " " * 16, "Exit the game")
                    turn_pl = False
                    run = False
                    # exit()
                    break
                elif shot_str == 'comp':  # debug cheat: if Player enter 'comp' -> turn go to the Computer
                    # print(shot_str)  # debug
                    turn_pl = False
                    turn_comp = True
                    break
                elif shot_str == 'win':  # debug cheat: if Player enter 'win' -> Player WIN! GAMEOVER
                    # print(shot_str)  # debug
                    score_pl = 18
                    print("Hey! You dirty little cheater =)")
                    break
                # Check input ERRORS
                # check that input is not empty and space
                elif shot_str == '' or shot_str == ' ':
                    print("Empty values. Enter coordinates from interval 1-10, please. Example: 7 3.")
                # check for some nums and spaces ' ' in input
                elif not set(shot_str) < (set([str(i) for i in range(10)]) | {' '}):
                    print("Incorrect values. Enter only two number with space, please. Example: 2 1.")
                else:
                    # check that input values is number in range 1-10
                    if set([int(i) for i in shot_str.split()]) < set(range(1, 11)):
                        xy_pl = [int(i) for i in shot_str.split()]  # get int num from shot_str
                        # check for repeating of coordinates
                        if xy_pl not in shots_story_pl:
                            shots_story_pl.append(xy_pl)
                            # agree shot and get X, Y from xy_pl list
                            player_shot_flag = True
                            x, y = xy_pl
                            x, y = x - 1, y - 1
                            # print("X & Y <= 10", x + 1, y + 1)  # debug
                            break
                        else:
                            print("Repeating values. You already shot in this coordinates. Enter new, please.")
                    else:
                        print("Incorrect values. Enter only two number from interval 1-10, please. Example: 5 10.")
                # break
            # some other input errors
            except:
                print("Incorrect values. Enter only two number for coordinates, please. Example: 9 10.")


        # Player get shot
        while player_shot_flag:
            player_shot = shots_func_3(x, y, shots_pl, fleet_comp, "Player", "Computer", num_turn_pl, score_pl, turn_pl)
            # print(x, y, "Player -> Computer", player_shot)  # debug
            turn_pl, num_turn_pl, score_pl = player_shot  # return result values of Player shot

            # Output results of shot
            print("Result:")
            print_fields_2("Player", "Computer", shots_comp, shots_pl, score_pl, score_comp, num_turn_pl,
                           num_turn_comp)  # show Players fleet and shots fields
            break

        # # player_shot_flag = False
        # run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func

        if turn_pl == False and run == True:
            turn_comp = True
            # player_shot_flag = False

    # Computer turn LOOP
    while turn_comp:
        x, y = xy_random()  # Generate random x & y coordinates from "xy_random" function
        # print("\n Computer shot in x y = ", x + 1, y + 1)  # debug

        comp_shot = shots_func_3(x, y, shots_comp, fleet_pl, "Computer", "Player", num_turn_comp, score_comp,
                                 turn_comp)  # Computer get shot
        # print(x, y, "Player -> Computer", comp_shot)  # debug
        turn_comp, num_turn_comp, score_comp = comp_shot  # return result values of Computer shot

        # Output results of shot
        print("Result:")
        print_fields_2("Player", "Computer", shots_comp, shots_pl, score_pl, score_comp, num_turn_pl,
                       num_turn_comp)  # show Players fleet and shots fields

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER

        if turn_comp == False and run == True:
            turn_pl = True
# quit()
exit()
