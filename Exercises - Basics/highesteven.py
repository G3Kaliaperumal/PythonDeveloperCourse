def highesteven(given_list):
    evenNumbers = []
    for number in given_list:
        if number % 2 == 0:
            evenNumbers.append(number)
    return max(evenNumbers)


# Printing the highest even number from the given list
print(highesteven([20, 45, 68, 97]))
