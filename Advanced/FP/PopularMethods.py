from functools import reduce

ones = [1, 2, 3, 4, 5]
tens = [10, 20, 30, 40, 50]
hundreds = [100, 200, 300, 400, 500]


# Map function
print(list(map(lambda item: item * 2, ones)))

# Filter function
print(list(filter(lambda item: item % 2 != 0, ones)))

# Zip function
print(list(zip(ones, tens, hundreds)))

# Reduce function
# => 1 * 2 * 3 * 4 * 5 = 120
print(reduce(lambda result, initial_value: result + initial_value, ones, 1))
