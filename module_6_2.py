class Vehicle:
    __COLOR_VARIANTS = ['red', 'yellow', 'orange', 'green', 'blue', 'purple', 'brown', 'gray', 'white', 'black']

    def get_color_variants(self):
        return self.__COLOR_VARIANTS

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):

        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        """ Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color,
        если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись:
        "Нельзя сменить цвет на <новый цвет>".
        Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black')."""
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)

    def get_passengers_limit(self):
        return self.__PASSENGERS_LIMIT


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()