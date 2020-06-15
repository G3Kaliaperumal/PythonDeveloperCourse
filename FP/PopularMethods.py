my_list = [1, 2, 3, 4, 5]


# Map function
def multiply_by_2(item):
    return item * 2


# Filter function
def find_odd_numbers(item):
    return item % 2 != 0


print(list(map(multiply_by_2, my_list)))
print(list(filter(find_odd_numbers, my_list)))
