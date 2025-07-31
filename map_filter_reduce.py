def cap_name(name):
    return name.capitalize()

def up_name(name):
    return name.upper()

names = ['alfatih','rayyan', 'budi', 'andi', 'salamah']

list_cap = []
for name in names:
    list_cap.append(cap_name(name))

print(list_cap)
print(up_name)

print('MAP')

map_cap = map(cap_name,names)
print(list(map_cap))

map_up = map(up_name,names)
print(list(map_up))

def even_nums(numbers):
    even_list = []

    for num in numbers:
        if num %2 == 0:
            even_list.append(num)
    
    print(even_list)

even_nums(range(1000))

print('FIlters')
def is_even(num):
    return num %2 == 0

numbers =(range(1000))
even_nums = filter(is_even,numbers)
print(list(even_nums))

from functools import reduce

def addition(number1, number2):
    return number1 + number2

hasil1 = addition(10,20)
print(hasil1)

num_list = range(1,11)
print(list(num_list))
total= reduce(addition, num_list)
print(total)

def multiplication(number1, number2):
    return number1 * number2

hasil2 = multiplication(10,20)
print(hasil2)

num_list2 = range(1,11)
print(list(num_list2))
total2 = reduce(multiplication, num_list2)
print(total2)

def countdown(number):
    print(number)
    if number == 0:
        return
    else:
        countdown(number-1)


countdown(10)

def faktorial(number):
    if number == 1:
        return 1
    else:
        result = number*faktorial(number-1)
        return result
    
lima = faktorial(5)
print(lima)