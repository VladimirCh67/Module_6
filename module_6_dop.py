from math import pi, sqrt


class Figure:
    def __init__(self,  __color , *__sides):
        self.__sides = __sides
        self.__color = __color
        self.filled = False

    sides_count = 0

    def get_color(self):

        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if self.r in range(0,255) and self.g in range(0,255) and self.b in range(0,255):
            return True
        else:
            return False


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [self.r, self.g, self.b]



    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count:
            x = True
            if isinstance(sides, tuple):
                for i in range(len(sides)):
                    if sides[i] < 0:
                        x = False
        else:
            self.__sides = []
            if self.sides_count == 12 and len(sides) == 1:
                a = sides[0]
            else:
                a = 1

            for i in range(self.sides_count):
                self.__sides.append(a)
            x = False

        return x


    def get_sides(self):

        return list(self.__sides)


    def __len__(self):
        prm = 0
        for i in range(self.sides_count):
            prm += self.__sides[i]

        return prm


    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = new_sides



class Circle(Figure):
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = __sides
        if isinstance(self.__sides, int):
            self.__radius = self.__sides / (2 * pi)


    def rad(self):
        print(round(self.__radius, 2))

    sides_count = 1

    def get_square(self):
        s = round((self.__radius ** 2) * pi, 2)
        return s


class Cube(Figure):
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__sides = __sides

    sides_count = 12

    def get_volume(self):
        if isinstance(self.__sides, int):
            v_ = self.__sides ** 3
        else:
            v_ = self.__sides[0] ** 3
        return v_

class Triangle(Figure):
    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.__sides = __sides

    sides_count = 3

    def get_square(self):
        a = self.__sides[0]
        b = self.__sides[1]
        c = self.__sides[2]

        # Формула Герона:
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))

        return s


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
triangle1 = Triangle((200, 200, 100), 10, 6, 8)
triangle2 = Triangle((200, 200, 100), 10, 6)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
print(circle1.get_color(), " Круг - цвет")
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color(), " Круг - цвет")
circle1.set_color(300, 70, 15) # Не изменится
print(circle1.get_color(), " Круг - цвет")
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color(), " Куб - цвет")
#print(circle1.perim())
circle1.rad()

# Проверка на изменение сторон
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides(), " Куб - стороны")
cube1.set_sides(5) # изменится
print(cube1.get_sides(), " Куб - стороны")
circle1.set_sides(15) # Изменится
print(circle1.get_sides(), " Круг - стороны")
circle1.set_sides(18, 10) # Изменится
print(circle1.get_sides(), " Круг - стороны")
triangle1.set_sides(18, 10) # Изменится
print(triangle1.get_sides(), " Треугольник - стороны")

circle1.get_color()

# Проверка периметра (круга), это и есть длина:
print(len(circle1), " Круг - периметр")

# Проверка площади (треугольника):
print(triangle1.get_square(), " Треугольник - площадь")
print(circle1.get_square(), " Круг - площадь")

# Проверка объёма (куба):
print(cube1.get_volume(), " Круг - объем")