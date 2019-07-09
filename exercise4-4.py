import random
num = random.randint(1, 10)
print('Pick a number between 1 and 10')
guess = int(input())
if guess == num:
    print('You Win!')
elif (guess - 1 == num) or (guess + 1 == num):
    print('So Close!')
else:
    print('Try Again')

print('The number was {}'.format(num))