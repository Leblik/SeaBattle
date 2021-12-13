# DEBUG

from all_func import *

print("\nDEBUG")

# start values
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

fleet_pl_2 = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
              [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
              [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Make int elmnts to str in fleets
fleet_pl = [[str(i) for i in row] for row in fleet_pl]
fleet_pl_2 = [[str(i) for i in row] for row in fleet_pl_2]

# Make fields of shots for Player 1 and Computer.
shots_pl_1 = [['~' for i in range(10)] for row in range(10)]
shots_comp = [['~' for i in range(10)] for row in range(10)]

score_pl = 0
score_comp = 0

# example of colored print
print('\x1b[1;34;48m'+'Y X'+'\x1b[0m')
print('\033[1;36;48m'+'Y X'+'\033[0m')
print("%2s%22s" % (10, 2356363463463))

# Colored strings by "colorama" module
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background' + Style.RESET_ALL)
print(f'{Fore.BLUE}and some green text{Style.RESET_ALL}')


# DEBUG function print_fields/print_fields_2/print_fields_3
print("print_fields")  # debug
print_fields("fleet_1_name", "fleet_2_name", fleet_pl, shots_pl_1, score_pl, score_comp)  # debug

shots_pl_1[0][3] = "X"
fleet_pl[1][0] = "o"

print("print_fields_2")  # debug
print_fields_2("fleet_1_name", "fleet_2_name", fleet_pl, shots_pl_1, score_pl, score_comp)  # debug
# all output is normal
print(shots_pl_1[0])
print(' '.join(shots_pl_1[0]))
print(fleet_pl[1])
print(" ".join(fleet_pl[1]))
# get formatted print
print("Formatted print:")
print('%2s%+23s%17s%25s' % (0, ' '.join(shots_pl_1[0]), 1, " ".join(fleet_pl[1])))
print(f'{1: >2} {" ".join(fleet_pl[1]): >23s} {1: >17} {" ".join(shots_pl_1[0]) :>23}')  # example of formatted output
print(f'{"10": >2} {" ".join(fleet_pl[1]): >23s} {"10": >23s} {" ".join(shots_pl_1[0]) :>23}')  # example of formatted output


# get colored
print("Colored shots_pl[4][1] = X (RED) & fleet_pl[1][2] = o (YELLOW)")
shots_pl_1[0][3] = f'{Fore.RED}X{Style.RESET_ALL}'
fleet_pl[1][0] = f'{Fore.YELLOW}o{Style.RESET_ALL}'
# shots_pl[0][3] = "X"
# fleet_pl[1][0] = "o"
print(shots_pl_1[0][3], fleet_pl[1][0])

print("print_fields")  # debug
print_fields("fleet_1_name", "fleet_2_name", fleet_pl, shots_pl_1, score_pl, score_comp)  # debug
# normal output

print("print_fields_2")  # debug
print_fields_2("fleet_1_name", "fleet_2_name", fleet_pl, shots_pl_1, score_pl, score_comp)  # debug

# BUG: have shift to left from 1st elem in printing of shots_pl
print(shots_pl_1[0])
print(" ".join(shots_pl_1[0]))
print(fleet_pl[1])
print(" ".join(fleet_pl[1]))
print("output string of fleet is normal...")
# get formatted print
print("but formatted print is not. Debug it:")
# print(f'{1: >2} {" ".join(fleet_pl[1]): >23s} {1: >17} {" ".join(shots_pl[0]) :>23}')  # example of formatted output
# print(f'{"10": >2} {" ".join(fleet_pl[1]): >23s} {"10": >23s} {" ".join(shots_pl[0]) :>23}')  # example of formatted output
ship_str_0 = '0 0 0 0 0 0 0 0 0 0'
ship_str_1 = " ".join(['~', '~', '~', '\x1b[31mX\x1b[0m', '~', '~', '~', '~', '~', '~'])
ship_str_2 = " ".join(['\x1b[33mo\x1b[0m', '0', '0', '0', '0', '0', '0', '0', '0', '0'])

print(ship_str_0)
print(ship_str_1)
print(ship_str_2)

# SUCCESS !!!
# var 1
print("var 1")
print(f"{10: <5} {ship_str_0: <19s}", ' '*15, f'{10: <5}{ship_str_1:<19}')  # example of formatted output
print(f'{10: <5} {ship_str_2: <19s}', ' '*15, f'{10: <5}{ship_str_1:<19}')  # example of formatted output

# var 2
print("var 2")
print("{:<5} {:19}".format(10, " ".join(['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'])),
      "{:<15}".format(" "),
      "{:<5} {:19}".format(10, " ".join(['~', '~', '~', '\x1b[31mX\x1b[0m', '~', '~', '~', '~', '~', '~'])))

print("{:<5} {:19}".format(10, " ".join(['\x1b[33mo\x1b[0m', '0', '0', '0', '0', '0', '0', '0', '0', '0'])),
      "{:<15}".format(" "),
      "{:<5} {:19}".format(10, " ".join(['~', '~', '~', '\x1b[31mX\x1b[0m', '~', '~', '~', '~', '~', '~'])))

# var 3
print("var 3")
print("{:<5} {:19}".format(10, ship_str_0),
      "{:<15}".format(" "),
      "{:<5} {:19}".format(10, ship_str_1))

print("{:<5} {:19}".format(10, ship_str_2),
      "{:<15}".format(" "),
      "{:<5} {:19}".format(10, ship_str_1))


# print('{:<5} {:<23}'.format(10, ship_str_2), ' '*15, '{:<5} {:<23}'.format(10, ship_str_1))
#
# print("{:<5} {:<23}".format(10, ship_str_2), end='')  # print fields
# print(" " * 15, end='')  # print fields
# print("{:<5} {:<23}".format(10, ship_str_1))  # print fields
