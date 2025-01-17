# В предыдущем задании "Homework_need_inheritance" Преподаватель потребовала доработать.

# Предыдущее задание было:

'''
Создайте:
2 класса родителя: Animal, Plant
Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения

4 класса наследника:
Mammal, Predator для Animal.
Flower, Fruit для Plant.

У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.

Метод eat должен работать следующим образом:
Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут
alive на False.
Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)

Создайте объекты классов и проделайте действия затронутые в примере результата работы программы.
'''

#    Пункты задачи:

# 1. Создайте классы Animal и Plant с соответствующими атрибутами и методами

# 2. Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
#    При необходимости переопределите значения атрибутов.

# 3. Создайте объекты этих классов.

############   Исправленный доработанный код:

# Родительский класс для животных
class Animal:
    alive = True  # Атрибут класса
    fed = False   # Атрибут класса

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                Animal.fed = True  # Изменяем атрибут класса
            else:
                print(f"{self.name} не стал есть {food.name}")
                Animal.alive = False  # Изменяем атрибут класса

# Родительский класс для растений
class Plant:
    edible = False  # Атрибут класса

    def __init__(self, name):
        self.name = name

# Класс Млекопитающих (наследник Animal)
class Mammal(Animal):
    pass

# Класс Хищников (наследник Animal)
class Predator(Animal):
    pass

# Класс Цветов (наследник Plant)
class Flower(Plant):
    pass

# Класс Фруктов (наследник Plant)
class Fruit(Plant):
    edible = True  # Фрукты съедобны по умолчанию (атрибут класса)

# Создание объектов и проверка
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(Animal.alive)  # Проверяем атрибут класса
print(Animal.fed)    # Проверяем атрибут класса

a1.eat(p1)  # Хищник пытается съесть цветок
a2.eat(p2)  # Млекопитающее съедает фрукт

print(Animal.alive)  # Волк умер
print(Animal.fed)    # Хатико сыт

# Вывод на консоль остался прежним: =>
'''
Волк с Уолл-Стрит
Цветик семицветик
True
False
Волк с Уолл-Стрит не стал есть Цветик семицветик
Хатико съел Заводной апельсин
False
True
'''