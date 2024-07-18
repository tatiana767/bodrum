'''Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.'''




class house:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')
        #self.__del__()


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'house: {self.name} floors:{self.number_of_floors}')

    def __str__(self):
        return (f'house: {self.name} floors:{self.number_of_floors}')

    def __len__(self):
        return self.number_of_floors

h1 = house('ЖК Эльбрус', 10)
print(house.houses_history)
h2 = house('ЖК Акация', 20)
print(house.houses_history)
h3 = house('ЖК Матрёшки', 20)
print(house.houses_history)

print(id(h2))    # Удаление объектов
del h2
print(id(h1))
del h3

print(house.houses_history)
