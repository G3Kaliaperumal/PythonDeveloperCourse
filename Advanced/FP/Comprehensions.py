# Comprehensions - easy way to create data structures rather than iterating over the list of elements


# List Comprehensions
# Printing numbers between 1 to 50(inclusive) that are divisible 5
result_list = [num for num in range(1, 51) if num % 5 == 0]
print(result_list)

# Set Comprehensions
result_set = {char for char in 'hello'}
print(result_set)

# Dictionary Comprehensions
result_dict = {num: num*2 for num in [1, 2, 3]}
print(result_dict)
