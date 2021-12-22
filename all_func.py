import sys
import random
from colorama import Fore, Back, Style
from playsound import playsound

# FUNCTIONS

# Function print_fields_2.
# Print 2 fields in one line in formatted strings with
# - ["".format(val)] and f'{val:form}';
# - colored strings. Var 1.
# + debug tab after shot in print_fields_2 func
def print_fields_2(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2, turn_count_1, turn_count_2):
    axis = list(range(1, 11))  # get range of axis
    print("\n"+f'{Fore.CYAN}{"Y": <5} {fleet_1_name + " fleet":>19}',
               f'{"Y":>17} {fleet_2_name + " fleet":>22s}{Style.RESET_ALL}')
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        ship_str_1 = " ".join([str(elem) for elem in ship_1])  # string of ships in fleet_1
        ship_str_2 = " ".join([str(elem) for elem in ship_2])  # string of ships in fleet_2
        print(f'{Fore.CYAN}{y: <5}{Fore.RESET} {ship_str_1: <19s}',
              ' ' * 15,
              f'{Fore.CYAN}{y: <5}{Fore.RESET}{ship_str_2:<19}')  # ver 5 - print fields
    x_axis = " ".join([str(x) for x in axis])  # get X - axis
    score_res_1 = '{} score: {} turn: {}'.format(fleet_1_name, str(score_count_1), str(turn_count_1))
    score_res_2 = '{} score: {} turn: {}'.format(fleet_2_name, str(score_count_2), str(turn_count_2))
    print("\n" + Fore.CYAN+'{:>4}{:>22}{:>19}{:>22}'.format("X", x_axis, "X", x_axis) + Fore.RESET)  # print x_axis
    print(Fore.YELLOW + "{:<22}{:>45}".format(score_res_1, score_res_2) + Fore.RESET)  # print scores
    print("-" * 70)


# Function xy_random return list of 2 various random number (range(0,9)) - coordinates x,y
def xy_random():
    randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
    return randomlist_2


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

# Function "gameover" check scores and return flag for end of game
def gameover(score_pl, score_comp):
    if score_pl == 18:
        print("          You WIN!")
        exit()
        return False
    elif score_comp == 18:
        print("         GAME OVER \n      Computer WIN!")
        exit()
        return False
    else:
        return True


# Example:
# run = gameover(score_pl, score_comp)  # check scores for GAMEOVER