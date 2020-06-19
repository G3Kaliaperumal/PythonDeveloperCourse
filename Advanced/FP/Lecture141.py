my_list = [5, 4, 3]

print(list(map(lambda number: number ** 2, my_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

print(list(sorted(a, key=lambda tupl: tupl[1])))
