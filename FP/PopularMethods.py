from functools import reduce

ones = [1, 2, 3, 4, 5]
tens = [10, 20, 30, 40, 50]
hundreds = [100, 200, 300, 400, 500]


# Map function
def multiply_by_2(item):
    return item * 2


# Filter function
def find_odd_numbers(item):
    return item % 2 != 0


# Reduce function
def multiplier(result, initial_value):
    return result * initial_value


print(list(map(multiply_by_2, ones)))
print(list(filter(find_odd_numbers, ones)))
# Zip function
print(list(zip(ones, tens, hundreds)))
print(reduce(multiplier, ones, 1))  # => 1 * 2 * 3 * 4 * 5 = 120
