some_list = ['a', 'b', 'g', 'a', 'n']

duplicates = list(
    set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)
