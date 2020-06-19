def add(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        return err
