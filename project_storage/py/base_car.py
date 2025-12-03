class Car():
    """Creating car class"""

    def __init__(self, model, year, engine_volume, price, mileage):
        """Initializing attributes of car"""
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description_car(self):
        """Receiving definition of car"""
        return f'Модель {self.model} {self.year} года, {self.wheels}-колёсный, с объёмом двигателя {self.engine_volume}л и пробегом {self.mileage}км стоит {self.price} денег' 
    
    def get_mileage(self):
        """Receiving mileage of car"""
        return f'Пробег на данный момент: {self.mileage} километров'

toyota = Car("Toyota", 2000, 2, 200000, 200000)
print(toyota.description_car())

