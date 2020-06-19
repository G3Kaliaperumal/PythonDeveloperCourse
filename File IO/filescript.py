test_file = open('test.txt')

# Note that python uses cursor so we can read file only once.
print(test_file.read())

# To reset the position of the start to the start, use seek(0)
# zero indicates the first index
test_file.seek(0)
print(test_file.read())

# Other methods:
# 1. readline()
test_file.seek(0)
line = test_file.readline()
while(line):
    print(line)
    line = test_file.readline()

# 2. readlines()
test_file.seek(0)
print(test_file.readlines())

test_file.close()
