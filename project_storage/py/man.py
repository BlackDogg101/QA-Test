import base_person 

man = base_person.Person("Alex", 30, 180)
man.description_person() 

warrior = base_person.Warrior("Conan", 32, 200)
# warrior.get_rage()
# warrior.update_weight(150)
# warrior.description_person()
print("Нового человека зовут " + warrior.description_person())
