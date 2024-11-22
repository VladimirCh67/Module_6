class Vehicle:
    owner = "Владелец"
    __model = "Модель"
    __engine_power = 0
    __color = "Цвет"
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']


    def get_model(self):
        print("Модель: " + self.__model)

    def get_horsepower(self):
        print("Мощность двигателя: " + str(self.__engine_power))

    def get_color(self):
        print("Цвет: " + self.__color)

    def print_info(self):
        print("*************")
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print("Владелец: " + self.owner)
        print("*************")

    def set_color(self, new_color):
        clr_var = self.__COLOR_VARIANTS
        x = True
        for i in range(len(clr_var)):
            if new_color.lower() == clr_var[i].lower():
                self.__color = new_color
                x = False

        if x:
            print("Нельзя сменить цвет на " + new_color)


class Sedan(Vehicle):

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self._Vehicle__model = model
        self._Vehicle__engine_power = engine_power
        self._Vehicle__color = color
        self.__PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
