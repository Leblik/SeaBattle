# DEBUG

from all_func import *

print("\nDEBUG")


str_1 = "10 2"
# str_shot = set(str_shot)
str_shot = set([int(i) for i in str_1.split()])
print(str_1)
print(str_shot)
print(set(range(11)))
print("num in 0-10", str_shot < set(range(11)))


run = True
input_player_flag = True

while run:
# Debug input coordinate
# shot_str player - input coordinates
# shot_str = input("\n Enter coordinate X Y (1-10) to make shot_str:")
# shot_str = (input("\n Enter coordinate X Y (1-10) to make shot_str:") if i not in list(', ;-'))
# x, y = (int(i) for i in input("\n Введите координаты x y через пробел ,;-:") if i not in list(', ;-'))
# x, y = (int(input("\n Введите координаты x y через пробел:")) for _ in range(2))

        # + add debug for false format of input coordinates
    player_shot_flag = False
    while input_player_flag:
        try:
            shot_str = input("\n Enter coordinate X & Y (1-10) to make shot_str:")
            if shot_str == 'n' or shot_str == 'q':  # quit the game
                print(shot_str)  # debug
                print("\n", " " * 16, "Exit the game")
                turn_pl = False
                run = False
                # exit()
                break
            elif shot_str == 'comp':  # debug cheat: if Player enter null string -> turn go to the Computer
                print(shot_str)  # debug
                turn_pl = False
                turn_comp = True
                break
            elif shot_str == 'win':  # debug cheat: if Player enter 'win' -> Player WIN! GAMEOVER
                print(shot_str)  # debug
                score_pl = 18
                print("Hey! You dirty little cheater =)")
                run = gameover(score_pl, score_comp)

            print("DEBUG: input string:", shot_str)  # debug
            xy_pl = [int(i) for i in shot_str.split()]  # get int num from shot_str
            # x, y = xy_pl
            # x, y = ((int(i) for i in shot_str) if i not in list(', ;-'))
            # x, y = x - 1, y - 1  # correct coordinate from human to machine, coze list[0, 1, 2 ...]
            # if x in set(range(10)) and y in set(range(10)):
            if set(xy_pl) < set(range(11)):
                x, y = xy_pl
                x, y = x - 1, y - 1
                print("X & Y <= 10", x+1, y+1)  # debug
                input_player_flag = False
                player_shot_flag = True
                # break
            else:
                print("ERROR. Enter right coordinates 0-10")
            break
        except:
            print("ERROR. Enter right coordinates")

    if player_shot_flag:
        print("player_shot_flag x, y:", x, y)  # debug
        break

# ORIGINAL
# if shot_str == 'n' or shot_str == 'q':  # quit the game
#     print(shot_str)  # debug
#     print("\n", " " * 16, "Exit the game")
#     turn_pl = False
#     run = False
#     # exit()
#     # break
# elif shot_str == 'comp':  # debug cheat: if Player enter null string -> turn go to the Computer
#     print(shot_str)  # debug
#     turn_pl = False
#     turn_comp = True
#     # break
# elif shot_str == 'win':  # debug cheat: if Player enter 'win' -> Player WIN! GAMEOVER
#     print(shot_str)  # debug
#     score_pl = 18
#     print("Hey! You dirty little cheater =)")
#     run = gameover(score_pl, score_comp)
# else:
#     print(shot_str)  # debug
#     xy_pl = [int(i) for i in shot_str.split()]
#     x, y = xy_pl
#     x, y = x - 1, y - 1  # correct coordinate from human to machine, coze list[0, 1, 2 ...]
#     player_shot_flag = True
#     print(x, y)

