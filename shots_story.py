# Algorithm for check last shots
# TODO: - make and add function for check current shot's coordinates
#  in list-story of last shots before get current shot

# Example
# shots_story_pl = [[2, 4], [10, 3], [9, 1]]  # list-story of last Player's shots
shots_story_pl = []  # list-story of last Player's shots

print("shots_story_pl:", shots_story_pl)

while True:
    shot_str = input("\n Enter coordinate X & Y (1-10) to make shot_str:") # current string shot of Player
    if shot_str == "q":  # Quit command
        break
    # xy_pl = "2 4 "  # current string shot of Player
    xy_pl = [int(i) for i in shot_str.split()]  # current string shot to list [X, Y]
    print("xy_pl = ", xy_pl)  # Debug
    print("Is xy_pl in shots_story_pl? :", xy_pl in shots_story_pl)
    if xy_pl not in shots_story_pl:
        shots_story_pl.append(xy_pl)
        print("Now xy_pl add to shots_story_pl")
        print("New shots_story_pl:\n", shots_story_pl)
    else:
        print("xy_pl is already in shots_story_pl!")
        print("Enter new coordinates X, Y")
        # break




