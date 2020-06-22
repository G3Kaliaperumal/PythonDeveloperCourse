import sys
from random import randint


def is_the_guess_correct(guess, answer, start, end):
    if guess < start or guess > end:
        print(f'Please only select numbers between {start} and {end}!')
        return False
    if answer == guess:
        print(f'Woah!! You are a genious ;)')
        return True
    else:
        print('Oops!! Try again')
        return False


if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    answer = randint(start, end)
    while True:
        try:
            guessed_number = int(
                input(f'Guess a number between {start} and {end}: '))
            result = is_the_guess_correct(guessed_number, answer, start, end)
            if result:
                break
            else:
                continue

        except:
            print('Input is invalid')
            continue
