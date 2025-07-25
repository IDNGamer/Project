print('Welcome to : Hobby To Dictionary!')
name = str(input('Name : '))
hobbies = str(input('Hobby (Use , to saperate items) : '))
function = str(input('Functions of your hobby (Use ,to saperate items) : '))

hobby = dict()

hobby['Name '] = name
hobby['Hobbies '] = hobbies
hobby['Function of hobbies '] = function
year = int(input('year : '))
place = str(input('place : '))
hobby['Year '] = year
hobby['Place '] = place


print(hobby)