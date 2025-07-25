def multiAddition(*numbers):
    result = 0
    for num in numbers:
        result += num 
        print(result)

multiAddition(1,2,3,4,5,6,7,8,9,0)
multiAddition(0,9,8,7,6,5,4,3,2,1)

def fullname (**data):
    for key, value in data.items():
        print(key, ':', value)

fullname(
    firstname = 'Alfatih',
    midname = 'Rayyan',
    lastname = 'Nugroho',
)

fullname(
    firstname = 'Alfatih',
    lastname = 'Nugroho',
    age = 12,
)
