import sys
from random import randint

start = int(sys.argv[1])
end = int(sys.argv[2])
answer = randint(start, end)
no_of_attempts = 0

while True:
    try:
        no_of_attempts += 1
        guessed_number = int(
            input(f'Guess a number between {start} and {end}: '))
        if guessed_number < start or guessed_number > end:
            print(f'Please only select numbers between {start} and {end}!')
            continue
        if answer == guessed_number:
            print(f'Woah!! You are a genious; No of guesses: {no_of_attempts}')
            break
        else:
            print('Oops!! Try again')
    except:
        print('Input is invalid')
        continue
