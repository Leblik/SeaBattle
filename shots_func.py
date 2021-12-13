import sys
from playsound import playsound


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
            # next Player(Computer) turn
            turn_shoter = False
    else:
        print("Повтор координат. Введите новые.")
    print("debug in shot_func:", turn_shoter, turn_count, score_count)  # debug
    return [turn_shoter, turn_count, score_count]  # return turn_pl/comp flag , turn counter and score counter


# Example:
# player_shot = shots_func(x, y, shots_pl, fleet_comp, "Player", "Computer", num_turn_pl, score_pl, turn_pl)  # Player get shot
#         print(x, y, "Player -> Computer", player_shot)  # debug
#         turn_pl, num_turn_pl, score_pl = player_shot
#
#         if not turn_pl:
#              turn_comp = True