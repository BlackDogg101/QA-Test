from base_person import Person

class Warrior(Person):
    """Creating warrior class"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряда ярости"""
        print('Заряд ярости : ' + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)
        # print("Нового человека зовут " + description)
        return description

warrior = Warrior("Conan", 32, 200)
print(warrior.description_person())