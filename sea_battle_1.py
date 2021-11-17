# Sea Battle Game
# Make by Leblik
#
# Beta version 0.1 of table game Sea Buttle.
#
# Поле игрока 1 и игрока 2 заданы изначально (10 x 10 клеток), пока что не меняются.
# В этой версии проверить механику выстрелов, отображения, записи и
# хранения резульатов выстрелов.

print("\n  Sea Battle Game \n ver.0.1")
# Make fields of fleets for player 1 and player 2.
# Ships in every fleet: x5 - 1, x4 - 1, x3 - 1, x2 - 2, x1 - 2
# 1 var - by hand
fleet_pl_1 = [[0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
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

# Change int elmnts to str in fleets
fleet_pl_1 = [[str(i) for i in row] for row in fleet_pl_1]
fleet_pl_2 = [[str(i) for i in row] for row in fleet_pl_2]

# Make fields of shots for player 1 and player 2.
shots_pl_1 = [['~' for i in range(10)] for row in range(10)]
shots_pl_2 = [['~' for i in range(10)] for row in range(10)]


# Function print_fields. Print 2 fields in one line
def print_fields(fleet_1_name, fleet_2_name, fleet_1, fleet_2):
    axis = list(range(1, 11))
    print("\nY   ",fleet_1_name,"field", " " * 17, fleet_2_name, "field")
    # print("v")
    for (y, ship_1, ship_2) in zip(axis, fleet_1, fleet_2):  # print y_axis and fleets
        print(y, "   ", ' '.join([str(elem) for elem in ship_1]), " " * 12, y,"  ", ' '.join([str(elem) for elem in ship_2]))
    x_axis = ' '.join([str(x) for x in axis])
    print("    X", x_axis, " " * 16, x_axis)   # print x_axis


# Game loop
run = True
while run:
    # print_fields("Player 1 fleet", "Player 2 fleet", fleet_pl_1, fleet_pl_2)    # show players fleets
    print_fields("Player 1 shots", "Player 2 shots", shots_pl_1, shots_pl_2)    # show players shots

#Player 1 make shot
# shot_pl_1 = input("Enter player 1 shot coordinate:").split()
    shot = input("\n Player 1 shot to X Y axis of Player 2:")

# quit the game
    if shot == 'q' or shot == 'q':
        run = False
        print("\n", " " * 16, "Exit the game")
        exit()

    shot_pl_1 = [int(i) for i in shot.split()]
# shot_pl_1 = shot_pl_1.split(',')
    print(shot_pl_1)  # debug
    x1, y1 = shot_pl_1
    x1, y1 = x1-1, y1-1  # correct coordinate from human to machine, coze list[0, 1, 2 ...]

    print("Player 1 fleet shot in x1, y1 = ", x1, "-", y1)  # debug

    if fleet_pl_2[y1][x1] == '1':  # y1 - num of column, x1 - num of elem in string
        print("Yehaaa! Ship is hit =)")
        fleet_pl_2[y1][x1] = 'X'
        shots_pl_1[y1][x1] = 'X'
    elif fleet_pl_2[y1][x1] == '0':
        print("You miss... ")
        fleet_pl_2[y1][x1] = '.'
        shots_pl_1[y1][x1] = '.'


# Print result of fire
# print_fields("Player 1 fleet", "Player 2 fleet", fleet_pl_1, fleet_pl_2)    # show player fleets
#     print_fields("Player 1 shots", "Player 2 shots", shots_pl_1, shots_pl_2)    # show player shots

# quit()
exit()
