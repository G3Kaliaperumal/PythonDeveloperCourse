# Do not worry about closing using the below approach of reading files
# Mode: 'r' -> read; 'w' -> write; 'r+' -> read and write; 'a' -> append;
with open('test.txt', mode='a') as test_file:
    text = '\nYippee!! darling'
    test_file.write(text)
