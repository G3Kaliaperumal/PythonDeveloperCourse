try:
    with open('sad.txt', mode='r') as input_file:
        print(input_file.read())
except FileNotFoundError as err:
    print('Oop!! File does not exists')
