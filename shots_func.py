import sys
import random
from playsound import playsound


# Function xy_random return list of 2 various random number (range(0,9)) - coordinates x,y
def xy_random():
    randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
    return randomlist_2


# Function shots_func get shots from input coordinates Player or Computer. WithOUT a colored chars.
def shots_func(x, y, shots_field, fleet_target, name_who_turn, name_target, turn_count, score_count, turn_shoter):
    if shots_field[y][x] == '~':  # check repeat of coordinates Player shot
        playsound(sys.path[1] + '\\sound\\rocket_1.mp3')  # playing rocket sound
        turn_count += 1  # counter of turns +1
        print(name_who_turn + " turns:", turn_count)  # debug
        if fleet_target[y][x] == '1':  # y - num of column, x - num of elem in string
            playsound(sys.path[1] + '\\sound\\bang_3s.mp3')  # playing rocket bang sound
            print(name_target + " ship is hit.")
            fleet_target[y][x] = 'X'  # not colored X
            shots_field[y][x] = 'X'  # not colored X
            score_count += 1  # player score counter +1
            turn_shoter = True
        elif fleet_target[y][x] == '0':
            playsound(sys.path[1] + '\\sound\\plop_1s.mp3')  # playing miss plop sound
            print("\n", name_who_turn + " miss... ")
            fleet_target[y][x] = 'o'  # not colored o
            shots_field[y][x] = 'o'  # not colored o
            turn_shoter = False  # next Player(Computer) turn
    else:
        print("Repeat coordinates. Enter new.")
    print("debug in shot_func:", turn_shoter, turn_count, score_count)  # debug
    return [turn_shoter, turn_count, score_count]  # return turn_pl/comp flag , turn counter and score counter


# Function shots_func_2 get shots from input coordinates Player or Computer.
# With a colored chars by ANSI "colorama" module.
# TODO: - debug tab after shot in shots_func_2 func
def shots_func_2(x, y, shots_field, fleet_target, name_who_turn, name_target, turn_count, score_count, turn_shoter):
    if shots_field[y][x] == '~':  # check repeat of coordinates Player shot
        playsound(sys.path[1] + '\\sound\\rocket_1.mp3')  # playing rocket sound
        turn_count += 1  # counter of turns +1
        print(name_who_turn + " turns:", turn_count)  # debug
        if fleet_target[y][x] == '1':  # y - num of column, x - num of elem in string
            playsound(sys.path[1] + '\\sound\\bang_3s.mp3')  # playing rocket bang sound
            print(name_target + " ship is hit.")
            fleet_target[y][x] = '\x1b[1;31;48m' + 'X' + '\x1b[0m'  # colored X
            shots_field[y][x] = '\x1b[1;31;48m' + 'X' + '\x1b[0m'  # colored X
            score_count += 1  # player score counter +1
            turn_shoter = True
        elif fleet_target[y][x] == '0':
            playsound(sys.path[1] + '\\sound\\plop_1s.mp3')  # playing miss plop sound
            print("\n", name_who_turn + " miss... ")
            fleet_target[y][x] = '\x1b[1;34;48m' + 'o' + '\x1b[0m'  # colored o
            shots_field[y][x] = '\x1b[1;34;48m' + 'o' + '\x1b[0m'  # colored o
            turn_shoter = False  # next Player(Computer) turn
    else:
        print("Repeat coordinates. Enter new.")
    print("debug in shot_func:", turn_shoter, turn_count, score_count)  # debug
    return [turn_shoter, turn_count, score_count]  # return turn_pl/comp flag , turn counter and score counter


# Function shots_func_3 get shots from input coordinates Player or Computer. With a colored chars by "colorama" module.
# add colored char "X" & "o" in shots_func
# debug tab after shot in shots_func_3 func
def shots_func_3(x, y, shots_field, fleet_target, name_who_turn, name_target, turn_count, score_count, turn_shoter):
    if shots_field[y][x] == Fore.BLUE + '~' + Fore.RESET or shots_field[y][x] == Fore.GREEN + 'A' + Fore.RESET:  #
        # check repeat of coordinates Player shot
        playsound(sys.path[1] + '\\sound\\rocket_1.mp3')  # playing rocket sound
        turn_count += 1  # counter of turns +1
        print(name_who_turn + " turns:", turn_count)  # debug
        if fleet_target[y][x] == '1':  # y - num of column, x - num of elem in string
            playsound(sys.path[1] + '\\sound\\bang_3s.mp3')  # playing rocket bang sound
            print(name_target + " ship is hit.")
            fleet_target[y][x] = f"{Fore.RED}X{Style.RESET_ALL}"  # colored RED X
            shots_field[y][x] = f"{Fore.RED}X{Style.RESET_ALL}"  # colored RED X
            score_count += 1  # score counter +1
            turn_shoter = True
        elif fleet_target[y][x] == '0':
            playsound(sys.path[1] + '\\sound\\plop_1s.mp3')  # playing miss plop sound
            print("\n", name_who_turn + " miss... ")
            fleet_target[y][x] = f"{Fore.YELLOW}o{Style.RESET_ALL}"  # colored o
            shots_field[y][x] = f"{Fore.YELLOW}o{Style.RESET_ALL}"  # colored o
            turn_shoter = False  # next Player(Computer) turn
    else:
        print("Repeat coordinates. Enter new.")
    # print("debug in shot_func:", turn_shoter, turn_count, score_count)  # debug
    return [turn_shoter, turn_count, score_count]  # return turn_pl/comp flag , turn counter and score counter


# Example:
# player_shot = shots_func(x, y, shots_pl, fleet_comp, "Player", "Computer", num_turn_pl, score_pl, turn_pl)  # Player get shot
#         print(x, y, "Player -> Computer", player_shot)  # debug
#         turn_pl, num_turn_pl, score_pl = player_shot
#
#         if not turn_pl:
#              turn_comp = True