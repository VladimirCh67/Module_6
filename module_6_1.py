class Animal:

    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat(self, food):
        self.food = food
        if self.food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:

    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass


class Fruit(Plant):
    def __init__(self, name, edible = True):
        self.edible = edible
        self.name = name



wolf = Predator('Волк')
sheep = Mammal('Баран')
rose = Flower('Роза')
banana = Fruit('Банан')

print(wolf.name)
print(rose.name, rose.edible)
print(banana.name, banana.edible)

print(wolf.name, "жив - ", wolf.alive)
print(sheep.name, "сыт - ", sheep.fed)

wolf.eat(rose)
sheep.eat(banana)

print(wolf.name, "жив - ", wolf.alive)
print(sheep.name, "сыт - ", sheep.fed)