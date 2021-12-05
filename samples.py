# SAMPLES
import sys
# import required module
from playsound import playsound
print("\nSAMPLES")
# Play sounds ____________________________________________________________________________
print("Project folder is", sys.path[1])  # Print current folder
# ________________________________________________________________________________________

# Play sounds ____________________________________________________________________________
# import required module
# from playsound import playsound

# for playing note.mp3 file
# playsound('E:/CODING/Python/Projects/SeaBattle/bang_2.mp3')
playsound(sys.path[1] + '\\sound\\bang_2s.mp3')  # SUCCESS !!! playing rocket shot
print('playing sound using  playsound')
# ________________________________________________________________________________________



# Format output print __________________________________________________________________
# ver 1
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# ver 2
print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
print('\x1b[6;31;42m' + 'Success!' + '\x1b[0m')
print("Bla bla bla")
print('\x1b[1;31;47m' + 'Success!' + '\x1b[0m')
print('\x1b[1;31;48m' + 'Success!' + '\x1b[0m')
print('\x1b[1;31;2m' + 'Success!' + '\x1b[0m')
"""
print('\x1b[style;string color;background-m' + 'Some string' + '\x1b[0m')
style = 0 - 8 
string color = 30 - 37
background = 40 - 48
 
"""


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(10):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(40, 49):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


# print_format_table()
# ________________________________________________________________________________________



# fleet_pl = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#               [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
#
# fleet_pl_2 = [[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
#               [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#               [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
#               [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
#
# # Make int elmnts to str in fleets
# fleet_pl = [[str(i) for i in row] for row in fleet_pl]
# fleet_pl_2 = [[str(i) for i in row] for row in fleet_pl_2]
#
#
# # Function print_fleets
# def print_fleets(fleet_1_name, fleet_2_name, fleet_1, fleet_2):
#     print("\n  ",fleet_1_name,"fleet", " " * 15, fleet_2_name, "fleet")
#     for (ship_1, ship_2) in zip(fleet_1, fleet_2):
#         print(' '.join([str(elem) for elem in ship_1]), " " * 10, ' '.join([str(elem) for elem in ship_2]))
#
#
# # print_fleets(fleet_pl, fleet_comp)  # call func
#
#
# # Make fields of shots for player 1 and player 2.
# shots_pl_1 = [['~' for i in range(10)] for row in range(10)]
# shots_pl_2 = [['~' for i in range(10)] for row in range(10)]
# print_fleets("Player 1", "Player 2", shots_pl_1, shots_pl_2)    # show shot result

# Player 1 make shot
# var 1
# shot_pl_1 = input("Enter player 1 shot coordinate:").split()
# shot_pl_1 = [int(i) for i in input("\n Введите координаты x y через пробел:").split(', |; ')]
# shot_pl_1 = shot_pl_1.split(',')
# print(shot_pl_1)  # debug
# x1, y1 = shot_pl_1
# x1, y1 = (int(input("\n Введите координаты x y через пробел:")) for _ in range(2))

# var 2
# x1, y1 = (int(i) for i in input("\n Введите координаты x y через пробел:") if i != ' ')  # только пробел
# x1, y1 = (int(i) for i in input("\n Введите координаты x y через пробел ,;-:") if i not in list(', ;-'))  # несколько вариантов разделителей
# print(x1, y1)   # debug
# print_fleets("Player 1", "Player 2", shots_pl_1, shots_comp)

# var 3
# import re
# shot_pl_1_new = re.split('[; ,]',input("\n Введите координаты x y через пробел:"))
# print(shot_pl_1_new)


# Содержание элемента в строке-списке
# A = list(', ;')
# print(A)
# x = ' '
# print("Содержится x ='", x,"' в A? - ", x in A)

# -------------------------------------------------------------
# fleet_pl = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#               [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#               [0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
#               [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
#               [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]]
# # Make int elmnts to str
# fleet_pl = [[str(i) for i in row] for row in fleet_pl]
#
# # fleet_pl_1_str = [[str(i) for j in range(m)] for i in range(n)]
# print(fleet_pl)  # debug
#
# Print 2 fleets in 1 line
# print("\n  Player 1 fleet", " "*15,"Player 2 fleet")
# for (ship_1, ship_2) in zip(fleet_pl, fleet_comp):
#     #print ("f: ", f ,"; b: ", b)
#     print(' '.join([str(elem) for elem in ship_1]), " "*10, ' '.join([str(elem) for elem in ship_2]))
#
# n, m = 10, 10
# d = [[0 for j in rage(m)] for i in range(n)]
# print(d) # debug
# for row in d: # output massiv
#    print(' '.join([str(elem) for elem in row]))
#
# c = [['.'] * n for i in range(n)] # make massiv n x n
# for elem in c:
#    c[0][1:6] = '1'*5
#    c[2][7:9] = '1'*2
# print("\n",c)
# for row in c: # debug output massiv c
#    print(' '.join([str(elem) for elem in row]))
#
# d = [[0]*n for i in range(n)] # make massiv n x n
# for elem in d:
#    d[0][3:6] = [1]*3
#    d[2][7:9] = [1]*2
# print("\n",d)
# for row in d: # debug output massiv c
#    print(' '.join([str(elem) for elem in row]))
#
# # Напечатать массив 2 способ
# for row in fleet_comp:
#    print(" "*10,*row)
# print()
# # Напечатать массив 3 способ
# [print(*i) for i in fleet_comp]

# Список рандомных значений
# import random
# # var 1. never list[0] != list[1]
# randomlist_1 = random.sample(range(0, 9), 2)  # never list[0] != list[1]
# print(randomlist_1)
#
# # var 2. maybe list[0] == list[1]
# randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
# x, y = randomlist_2
# print(x, y)
#
# # Function xy_random generate 2 number - coordinates in range(0,9)
# def xy_random():
#     randomlist_2 = [random.randint(0, 9) for i in range(2)]  # maybe list[0] == list[1]
#     return randomlist_2
#
#
# x, y = xy_random()
# print(x, y)
