while True:
    try:
        age = int(input('What is your age?'))
        100 / age
    except ValueError:
        print('Please enter a number')
    except:
        print('Please enter a valid number(Not 0 please)')
    else:
        print(f'Your age is {age}')
        break
