# Pure Function because it does not access the outside variables or does other functionalities
# It does the work of what it is intended to do and always produces the same result for the same input
# For example: If the return statement were `return print(new_list)`, then the function is not pure
# as it prints the output on the screen
def doubleTheNumbers(given_list):
    new_list = []
    for number in given_list:
        new_list.append(number * 2)
    return new_list


print(doubleTheNumbers([1, 2, 3]))
