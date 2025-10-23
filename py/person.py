class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        """Просим человека спеть"""
        print(self.name + ' поёт')

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + ' танцует')


man = Person('Алекс', 30)
woman = Person('Алла', 28)
#print(man.name)

man.dance()
woman.sing()
