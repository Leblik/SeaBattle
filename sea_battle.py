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

print("\n  Sea Battle Game \n ver.0.4"
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


# GAME LOOP
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
# show Players fleet and shots fields
print_fields_2("Player", "Computer", shots_comp, shots_pl, score_pl, score_comp, num_turn_pl, num_turn_comp)

while run:

    # Player turn
    while turn_pl and run:

        # Player input coordinates
        # + add debug for false format of input coordinates
        player_shot_flag = False
        try:
            # input string of coordinates X Y
            shot_str = input("\n Enter coordinate X & Y (1-10) to make shot_str:")

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
                # break
            else:
                xy_pl = [int(i) for i in shot_str.split()]  # get int num from shot_str
                if set(xy_pl) < set(range(11)):  # check x, y in range 1-10
                    player_shot_flag = True  #
                    x, y = xy_pl
                    x, y = x - 1, y - 1
                    # print("X & Y <= 10", x + 1, y + 1)  # debug
                else:
                    print("ERROR. Enter right coordinates 0-10")
            # break
        except:
            print("ERROR. Enter right coordinates")

        # Player get shot
        while player_shot_flag:
            player_shot = shots_func_3(x, y, shots_pl, fleet_comp, "Player", "Computer", num_turn_pl, score_pl, turn_pl)
            # print(x, y, "Player -> Computer", player_shot)  # debug
            turn_pl, num_turn_pl, score_pl = player_shot  # return result values of Player shot

            # Output results of shot
            print_fields_2("Player", "Computer", shots_comp, shots_pl, score_pl, score_comp, num_turn_pl,
                           num_turn_comp)  # show Players fleet and shots fields
            break

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func

        if turn_pl == False and run == True:
            turn_comp = True
            # player_shot_flag = False

    # Computer turn
    while turn_comp:
        x, y = xy_random()  # Generate random x & y coordinates from "xy_random" function
        # print("\n Computer shot in x y = ", x + 1, y + 1)  # debug

        comp_shot = shots_func_3(x, y, shots_comp, fleet_pl, "Computer", "Player", num_turn_comp, score_comp,
                                 turn_comp)  # Computer get shot
        # print(x, y, "Player -> Computer", comp_shot)  # debug
        turn_comp, num_turn_comp, score_comp = comp_shot  # return result values of Computer shot

        print_fields_2("Player", "Computer", shots_comp, shots_pl, score_pl, score_comp, num_turn_pl, num_turn_comp)  # show Players fleet and shots fields

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER

        if turn_comp == False and run == True:
            turn_pl = True
# quit()
exit()
