

# Function print_fields. Print 2 fields in one line
def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2):
    axis = list(range(1, 11))
    print("\nY      ", fleet_1_name, "fleet", " " * 25, fleet_2_name, "fleet")
    # print("v")
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        print(y, "   ", ' '.join([str(elem) for elem in ship_1]), " " * 12, y, "  ",
              ' '.join([str(elem) for elem in ship_2]))
    x_axis = ' '.join([str(x) for x in axis])
    print("    X", x_axis, " " * 16, x_axis)  # print x_axis
    print("       ", fleet_1_name + " score:", score_count_1, " "*23 + fleet_2_name + " score:", score_count_2)
    print("-" * 70)
    # TODO: make print with format


# Make fields of shots for player 1 and player 2.
# shots_pl = [['~' for i in range(10)] for row in range(10)]
# shots_pl_2 = [['~' for i in range(10)] for row in range(10)]

# Example:
# print_fields("Player 1 shots", "Player 2 shots", shots_pl, shots_pl_2)


# Перебираем элементы списка циклом for в столбик
# y_axis = list(range(1, 11))
# for elem in y_axis:
#     print(" " * 7, elem, end="\n")

# Перебираем элементы списка циклом for в строчку
# x_axis = list(range(1, 11))
# print("\n", " " * 12, end='')
# for elem in x_axis:
#     print(elem, end=' ')
# print('\n')