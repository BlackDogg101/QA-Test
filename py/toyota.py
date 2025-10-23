from base_car import Car

class Truck(Car):
    """Создание класса-наследника"""

    def __init__(self, model, year, engine_volume, price, mileage):
        """Инициализируем атрибуты класса-наследника"""
        super().__init__(model, year, engine_volume, price, mileage)
        self.wheels = 8


belaz = Truck("BelAZ", 2013, 165, 1000000, 2000)
print(belaz.description_car())
# print(belaz.get_mileage())