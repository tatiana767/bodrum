'''Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}'''

import inspect
from pprint import pprint


class Object_1:
     def __init__(self):
         self.param1 = 'stroka'
         self.param2 = 123
         self.param3 = [x  for x in range(0, 10)]

     def func1(self):
         print (self.param1)

     def func2(self):
         print(self.param2)
     def func3(self):
         print(self.param3)


def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attr'] = []
    info['methods'] = []
    info['module'] = inspect.getmodule(obj)

    for i in inspect.getmembers(obj):
       if  str(i[1]).find('method') != -1:
           #print(i[0], "- метод")
           info['methods'].append(str(i[0]))
       else:
           info['attr'].append(str(i[0]))
    print('info about :', obj)


    return(info)

C = Object_1()

pprint(introspection_info(C))

pprint(introspection_info(1234))


