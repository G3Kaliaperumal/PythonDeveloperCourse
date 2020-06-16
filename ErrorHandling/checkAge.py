while True:
    try:
        age = int(input('What is your age?'))
        100 / age
        raise TypeError('Oops')
    except (ValueError, ZeroDivisionError):
        print('Please enter a number')
    except:
        print('Some runtime exception has occurred :(')
    else:
        print(f'Your age is {age}')
        break
    finally:
        print('I am always watching you...')
