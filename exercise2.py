# this is my tip calculator

print('What was the bill?')
price = float(input())
print('What type of tip do you want to give? Poor, good, or great')
tip_amount = str(input()).lower()

if tip_amount == 'poor':
    tip = round(price * .10, 2)
elif tip_amount == 'good':
    tip = round(price * .18, 2)
elif tip_amount == 'great':
    tip = round(price * .25, 2)

print('This is a {} tip ${}'.format(tip_amount, tip))

# Try adding a string and an integer

print(int('7') + 7)

#string interpolation

print('Give me a big number:')
first_number = int(input())
print('Give me another number:')
second_number = int(input())
result = first_number * second_number
print('{} multiplied buy {} equals {}'.format(first_number, second_number, result))

# this equals true

print((10 < 20 and 30 < 20) or not(10 == 11))