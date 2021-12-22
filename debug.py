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
turn_pl = True  # Player turns first
turn_comp = False  # Computer turns if Player miss
# input_player_flag = True
player_shot_flag = False

while run:
# Debug input coordinate
# shot_str player - input coordinates
# shot_str = input("\n Enter coordinate X Y (1-10) to make shot_str:")
# shot_str = (input("\n Enter coordinate X Y (1-10) to make shot_str:") if i not in list(', ;-'))
# x, y = (int(i) for i in input("\n Введите координаты x y через пробел ,;-:") if i not in list(', ;-'))
# x, y = (int(input("\n Введите координаты x y через пробел:")) for _ in range(2))

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


        if player_shot_flag:
            print("player_shot_flag x, y:", x, y)  # debug
            turn_pl = False
            run = False
            break

# exit()


