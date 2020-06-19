def add(num1=0, num2=0):
    try:
        return num1 + num2
    except TypeError as err:
        return err
