# Function shots_func get shots from input coordinates Player or Computer


def shots_func(x, y, shots_field, target_fleet, name_who_turn, target_name):
    if shots_field[y][x] == '~':  # check repeat of coordinates Player shot
        if target_fleet[y][x] == '1':  # y1 - num of column, x1 - num of elem in string
            print(target_name + " ship is hit.")
            target_fleet[y][x] = 'X'
            shots_field[y][x] = 'X'
        elif target_fleet[y][x] == '0':
            print(name_who_turn + " miss... ")
            target_fleet[y][x] = '.'
            shots_field[y][x] = '.'
            # next Player(Computer) turn
    else:
        print("Повтор координат. Введите новые.")

# Example:
# shots_func(4, 1, shots_pl_1, fleet_comp, Player)

