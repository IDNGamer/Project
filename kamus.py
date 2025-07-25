students = {
    "name" : "Alfatih",
    "age" : 11,
    "address" : "Indonesia",
}

print(students)
print(type(students))

print(students.keys())
print(students["address"])


students['subject_favourite'] = ['science', 'IT']
students['address'] = "Tanggerang"
print(students)

students.pop("age")
students.popitem()
print(students)

student2 = dict(name = "Alfatih", age = 11)
print(student2)