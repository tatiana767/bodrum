'''Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
Пункты задачи:
Создайте класс House.
Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
Создайте объект класса House с произвольным названием и количеством этажей.
Вызовите метод go_to у этого объекта с произвольным числом.'''



class house:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        print(f'house: {name} floors:{number_of_floors}')

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("this floor doesn't exist")
        else:
            for i in range(1, new_floor):
                print(i)


orlov = house("JK ORLOV", 25)
orlov.go_to(30)
orlov.go_to(-1)
orlov.go_to(5)
