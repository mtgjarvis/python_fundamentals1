distance = 0
walk_rate = 1
run_rate = 5
energy = 10

print('Would you like to walk or run or go home?')
mode_trans = input().lower()
while energy > 0:
    if mode_trans == 'walk':
        distance = distance + 1
        energy = energy + 1
        print('Distance from home is {} and your energy is {}'.format(distance, energy))
    elif mode_trans == 'run':
        distance = distance + 5
        energy = energy - 2
        print('Distance from home is {} and your energy is {}'.format(distance, energy))
    elif mode_trans == 'eat':
        energy = energy + 3
        print('Your energy is now {}'.format(energy))
    elif mode_trans == 'rest':
        energy = energy + 1
        print('Your energy is now {}'.format(energy))
    elif mode_trans == 'go home':
        print('User went home')
        break
    else:
        print('You have not entered a correct choice')

    print('Would you like to walk or run eat or rest?')
    mode_trans = input().lower()

