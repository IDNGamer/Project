# create a variable called 'numbers'
numbers = (range)
# create a list of numbers 1 - 250 using list(range())
numbers = (range(1,251))
# print a number from index 15
print(numbers[15])


# print an eight number from the back
print(numbers[-8])
# clue : negative indexing
print('this number printed to your screen thanks to negative number indexing')


# print a group of numbers, start from 55 until 67
print(list(numbers[54:67]))


# print a group of even numbers, starts from 70 until 240
print(list(numbers[69:241:2]))
# clue : use step parameter
print('this number printed to your screen thanks to step parameter')

