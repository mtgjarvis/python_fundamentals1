distance = 0
walk_rate = 1
run_rate = 5

print('Would you like to walk or run?')
mode_trans = input().lower()
while mode_trans == 'walk' or mode_trans == 'run':
    if mode_trans == 'walk':
        distance = distance + 1
        print('Distance from home is {}'.format(distance))
    elif mode_trans == 'run':
        distance = distance + 5
        print('Distance from home is {}'.format(distance))
    print('Would you like to walk or run?')
    mode_trans = input().lower()

