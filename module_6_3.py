from random import randint


class Animal:
    def __init__(self, speed =0, _cords = [0, 0, 0]):
        self._cords = _cords
        self.speed = speed

    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def move(self, dx, dy, dz):
        self._cords[0] += self.speed * dx
        self._cords[1] += self.speed * dy
        self._cords[2] += self.speed * dz


    def speak(self):
        print(self.sound)

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def get_cords(self):
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")



class Bird(Animal):
    def __init__(self, _cords):
        super().__init__(_cords)
        self._cords = _cords

    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, _DEGREE_OF_DANGER):
        super().__init__(_DEGREE_OF_DANGER)
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._cords[2] -= int(self.speed/2 * abs(dz))


class PoisonousAnimal(Animal):
    def __init__(self, _DEGREE_OF_DANGER):
        super().__init__(_DEGREE_OF_DANGER)
    _DEGREE_OF_DANGER = 8



class Duckbill( Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed, _cords = [0, 0, 0]):
        self.speed = speed
        self._cords = _cords

    sound = "Click-click-click"

#print(Duckbill.mro())

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()

db.attack()

db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()

db.lay_eggs()

