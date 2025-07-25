fruits = {"apple", 'banana', "cherry", 'apple'}
print(fruits)
print(type(fruits))

for fruit in fruits:
    print(fruit)

fruits.add('lychee')
print(fruits)

fruits.discard('watermelon')
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.pop
print(fruits)

someotherfruits = ["grape", "manggo"]

fruits.update(someotherfruits)
print(fruits)