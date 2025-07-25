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