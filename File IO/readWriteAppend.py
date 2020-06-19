# Do not worry about closing using the below approach of reading files
# Mode: 'r' -> read; 'w' -> write; 'r+' -> read and write; 'a' -> append;
# Relative path: files\\test.txt
# Absolute path: C:\\Users\\kaga9005\\Documents\\Udemy\\Complete Python Developer\\File IO\\files\test.txt
with open('files\\test.txt', mode='r') as test_file:
    print(test_file.read())
