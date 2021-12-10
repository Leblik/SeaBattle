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
# from all_func import print_fields, xy_random, shots_func, gameover
from all_func import *


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
            print("Hey! You dirty little cheater =)")
            run = gameover(score_pl, score_comp)
        else:
            xy_pl = [int(i) for i in shot.split()]
            x, y = xy_pl
            x, y = x - 1, y - 1  # correct coordinate from human to machine, coze list[0, 1, 2 ...]

        # run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func
        if turn_pl == False and run == True:
            turn_comp = True

        # Player get shot
        player_shot = shots_func(x, y, shots_pl_1, fleet_comp, "Player", "Computer", num_turn_pl, score_pl, turn_pl)
        print(x, y, "Player -> Computer", player_shot)  # debug
        turn_pl, num_turn_pl, score_pl = player_shot  # return result values of Player shot
        # Output results of shot
        print_fields("Player", "Computer", fleet_pl, shots_pl_1, score_pl, score_comp)  # show Players fleet and shots fields

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER func

        if turn_pl == False and run == True:
            turn_comp = True


# Computer turn
    while turn_comp:
        x, y = xy_random()  # Generate random x & y coordinates from "xy_random" function
        # print("\n Computer shot in x y = ", x + 1, y + 1)  # debug

        comp_shot = shots_func(x, y, shots_comp, fleet_pl, "Computer", "Player", num_turn_comp, score_comp,
                               turn_comp)  # Computer get shot
        print(x, y, "Player -> Computer", comp_shot)  # debug
        turn_comp, num_turn_comp, score_comp = comp_shot  # return result values of Computer shot

        print_fields("Player", "Computer", fleet_pl, shots_pl_1, score_pl, score_comp)  # show Players fleet and shots fields

        run = gameover(score_pl, score_comp)  # check scores for GAMEOVER

        if turn_comp == False and run == True:
            turn_pl = True
# quit()
exit()
