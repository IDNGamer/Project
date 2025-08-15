
class animal:
    name = ""
    color = ""

    def __init__(self, name_animal, color_animal):
        self.name = name_animal
        self.color = color_animal
    def makeSound(self, sound):
        print('it is making a', sound)

    def eat(self, food):
        print(self.name, 'is eating', food)


cat = animal('Tom', 'Blue')
cat.name = "Tom"
cat.color = "Blue"
print(cat.name, cat.color)
print(type(cat))
cat.makeSound('Miaw')
cat.eat('Fish')

mouse = animal('Jerry', 'Grey')
mouse.name = "Jerry"
mouse.color = "Grey"
print(mouse.name, mouse.color)
print(type(mouse))
mouse.makeSound('Cikitcikit')
mouse.eat('Nuts')

fish = animal('Nemo', 'Orange')
fish.name = ('Nemo')
fish.color = ('Orange')
print(fish.name, fish.color)
print(type(fish))
fish.makeSound('---')
fish.eat('Pellets')