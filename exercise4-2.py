my_age = 40
print('How old are you?')
their_age = int(input())
years_apart = abs(my_age - their_age)

if their_age > 105:
    print("I'm not sure I believe you")
else:
    print('We are {} years apart'.format(years_apart))