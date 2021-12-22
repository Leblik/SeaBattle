
# Function print_fields. Print 2 fields in one line
def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2):
    axis = list(range(1, 11))
    print("\nY      ", fleet_1_name, "fleet", " " * 25, fleet_2_name, "fleet")
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        print(y, "   ", " ".join([str(elem) for elem in ship_1]), " " * 12, y, "  ",
              " ".join([str(elem) for elem in ship_2]))
    x_axis = " ".join([str(x) for x in axis])
    print("    X", x_axis, " " * 16, x_axis)  # print x_axis
    print("       ", fleet_1_name + " score:", score_count_1, " "*23 + fleet_2_name + " score:", score_count_2)  # print scores
    print("-" * 70)


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
    # score_res_2 = fleet_2_name + " score: " + str(score_count_2)
    print("\n" + Fore.CYAN+'{:>4}{:>22}{:>19}{:>22}'.format("X", x_axis, "X", x_axis) + Fore.RESET)  # print x_axis
    print(Fore.YELLOW + "{:<22}{:>45}".format(score_res_1, score_res_2) + Fore.RESET)  # print scores
    print("-" * 70)


# Function print_fields_3. Print 2 fields in one line in formatted strings with ["%" % (val)]. Var 2.
# TODO: - debug tab after shot in print_fields_3 and shots_func func
def print_fields_3(fleet_1_name, fleet_2_name, fleet_1, fleet_2, score_count_1, score_count_2):
    axis = list(range(1, 11))  # get range of axis
    print('\n' + '%2s%23s%17s%25s' % ("Y", fleet_1_name + " fleet", "Y", fleet_2_name + " fleet"))

    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        ship_str_1 = ' '.join([str(elem) for elem in ship_1])  # string of ships in fleet_1
        ship_str_2 = ' '.join([str(elem) for elem in ship_2])  # string of ships in fleet_2
        print('%5s%19s%19s%19s' % (y, ship_str_1, y, ship_str_2))  # print fields

    x_axis = ' '.join([str(x) for x in axis])  # get X - axis
    score_res_1 = fleet_1_name + " score: " + str(score_count_1)
    score_res_2 = fleet_2_name + " score: " + str(score_count_2)
    print('\n' + '%4s%22s%20s%22s' % ("X", x_axis, "X", x_axis))  # print x_axis
    print('%22s%45s' % (score_res_1, score_res_2))  # print scores
    print("-" * 70)


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