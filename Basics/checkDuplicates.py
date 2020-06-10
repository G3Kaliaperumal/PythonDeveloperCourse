my_list = ['a', 'b', 'c', 'a', 'n', 'n', 'm']
duplicates = []

for char in my_list:
    if my_list.count(char) > 1:
        if char not in duplicates:
            duplicates.append(char)

print(duplicates)
