import sys
import random
from playsound import playsound

# FUNCTIONS
# Function print_fields. Print 2 fields in one line
def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2):
    axis = list(range(1, 11))
    print("\nY      ", fleet_1_name, "fleet", " " * 25, fleet_2_name, "fleet")
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        print(y, "   ", ' '.join([str(elem) for elem in ship_1]), " " * 12, y, "  ",
              ' '.join([str(elem) for elem in ship_2]))
    x_axis = ' '.join([str(x) for x in axis])
    print("    X", x_axis, " " * 16, x_axis)  # print x_axis
    print("       ", fleet_1_name + " score:", score_count_1, " "*23 + fleet_2_name + " score:", score_count_2)  # print scores
    print("-" * 70)


# Function print_fields_2. Print 2 fields in one line in formatted strings
# TODO: debug after shot in print_fields_2 func
def print_fields_2(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2):
    axis = list(range(1, 11))  # get range of axis
    print('\n'+'{:>2}{:>23}{:>17}{:>25}'.format("Y", fleet_1_name + " fleet","Y", fleet_2_name + " fleet"))
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        ship_str_1 = ' '.join([str(elem) for elem in ship_1])  # string of ships in fleet_1
        ship_str_2 = ' '.join([str(elem) for elem in ship_2])  # string of ships in fleet_2
        print('{:>2}{:>23}{:>17}{:>25}'.format(y, ship_str_1, y, ship_str_2))  # print fields
    x_axis = ' '.join([str(x) for x in axis])  # get X - axis
    score_res_1 = fleet_1_name + " score: " + str(score_count_1)
    score_res_2 = fleet_2_name + " score: " + str(score_count_2)
    print('\n'+'{:>4}{:>22}{:>20}{:>22}'.format("X", x_axis, "X", x_axis))  # print x_axis
    print('{:<22}{:>45}'.format(score_res_1, score_res_2))  # print scores
    print("-" * 70)



# Function xy_random return list of 2 various random number (range(0,9)) - coordinates x,y
def xy_random():
    randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
    return randomlist_2


# Function shots_func get shots from input coordinates Player or Computer
def shots_func(x, y, shots_field, fleet_target, name_who_turn, name_target, turn_count, score_count, turn_shoter):
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
        print("Повтор координат. Введите новые.")
    print("debug in shot_func:", turn_shoter, turn_count, score_count)  # debug
    return [turn_shoter, turn_count, score_count]  # return turn_pl/comp flag , turn counter and score counter

# Function "gameover" check scores and return flag for end of game
def gameover(score_pl, score_comp):
    if score_pl == 18:
        print("          You WIN!")
        # return False
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