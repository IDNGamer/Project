def average(*numbers):
    result = 0
    for num in numbers:
        result += num

    avg = result / len(numbers)
    print(avg)

average(1, 10)