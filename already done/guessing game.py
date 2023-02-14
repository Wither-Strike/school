import random
finishtrue = None
number = random.randint(1,10)
while finishtrue != 1:
    guess = int(input('1-10 '))
    if guess == number:
        print('you win')
        finishtrue = 1
    elif guess < number:
        print('too low')
    else:
        print('too high')
