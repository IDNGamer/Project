class Person:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"This person's name {self.name}")

person1 = Person('Fatih')
person1.info()

person1 = Person('Rayyan')
person1.info()

class Student(Person):
    def __init__(self, name, nis):
        super().__init__(name)
        self.nis = nis

    def study(self, subject):
         print(f"{self.name} with nis {self.nis} study {subject}")

    def info(self):
        Person.info(self)
        print(f"NIS : {self.nis}")


student1 = Student("Alif", '0001')
student1.info()
student1.study('Math')
