'''


Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)
Метод get_square возвращает площадь треугольника.
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.


'''
from math import sqrt
class Figure:

    sides_count = 0
    filled = False

    def __init__(self, RGB, *argv ):
        self.__sides = []
        #print('количество сторон', self.sides_count)
        if self._is_valid_color(RGB):
            self.set_color(*RGB)
        #print('RGB:', RGB, '*argv:', argv, len(argv))

        if isinstance(self, Cube ) and len(argv)==1 and argv[0] > 0  :
               #print ('Cube!', self.__sides)
               for i in range(0, self.sides_count):
                   self.__sides.append(argv[0])
               #print('Cube!!', self.__sides)
        else:
               if self.__is_valid_sides(*argv):
                  #print('valid',self.__is_valid_sides(*argv) )
                  self.set_sides(*argv)
               else:
                  for i in range(0, self.sides_count):
                     self.__sides.append(1)
       

    def get_color(self):
        return self.__color

    def _is_valid_color(self, RGB):
        if isinstance(RGB, tuple) and len(RGB)==3:
            for i in RGB:
                if i >= 0 and i <= 255:
                    return True
                else:
                    return False
        else:
            return False

        pass

    def set_color(self, r, g, b):
        RGB = (r,g,b)

        if self._is_valid_color(RGB):
           self.__color = [r, g, b]


    def __is_valid_sides(self, *argv):

        if (len(argv)) == self.sides_count :

            for i in argv:
               # print('hey',i)
                if i >= 0: 
                    pass
                else:
                    return False
        else: 
            return False
       
        return True 
            


    def get_sides(self):
        return list(self.__sides)

    def set_sides(self, *new_sides):

        if len(new_sides) == self.sides_count and self.__is_valid_sides( *new_sides):
            self.__sides = new_sides

    def __len__(self):
        res = 0
        for i in self.__sides:
            res += i
        return res    

class Circle(Figure):

    def __init__(self, RGB, *argv):
        self.sides_count = 1
        super().__init__(RGB, *argv)
        #print('side: ', self.get_sides()[0])
        self.__radius =self.get_sides()[0]/(2*3.14)
        #print('radius = ', self.__radius)

    def get_square(self):
        return 3.14*(self.__radius**2)



class Triangle(Figure):

    def __init__(self, RGB, *argv):
        #print('#', *argv, len(argv))
        self.sides_count = 3
        super().__init__(RGB, *argv)
        #print('square', self.get_square())
        self.__height = 2*self.get_square()/self.get_sides()[0]

    def get_square(self):
        p = sum(self.get_sides()) / 2
        #print('p=', p)
        a = self.get_sides()
        #print(a[0], a[1], a[2])
        p = (p * (p - a[0]) * (p - a[1]) * (p - a[2]))
        if p > 0 :
            square  = sqrt(p)
            return square
        else :
            print("такого треугольника не сушествует")

    def get_height(self):
        return self.__height







class Cube(Figure):

    def __init__(self, RGB, *argv):
        self.__sides = []
        #print('#', *argv, len(argv))
        self.sides_count = 12
        super().__init__(RGB, *argv)

    def set_sides(self,  *new_sides):
        self.__sides = []
        if len(new_sides) == 1 and new_sides[0] > 0:
            for i in range(0, len(new_sides)):
               __sides.append(new_sides[0])
      #  else :
      #      if len(new_sides) > 1:
      #          for i in range(0, len(new_sides)):
      #              self._Cube__sides.append(1)

    def get_sides(self):
        if self.__sides == []:
            self.__sides = self._Figure__sides

        return self.__sides


    def get_volume(self):
        if self.__sides == []:
            self.__sides = self._Figure__sides
        #print (self.__sides)
        return self.get_sides()[0]**3




if __name__ == '__main__':
   ''' print('мы тут')
    a1 = Circle((200,200,200),3)
    f = a1.get_square()
    print('colors = ', a1.get_color())
    print('square = ', f)
    a1.set_color(100,200,1)
    print('colors = ', a1.get_color())
    c1 = Triangle((2,3,4),4)
    print(c1.get_sides(), c1.get_color())


    b1 = Triangle((20, 20, 20), 3, 2, 3)
    print('colors = ', b1.get_color())
    b1.set_sides(4,7,8)
    print('sides', b1.get_sides())

    b1.set_sides(4,7,-8)
    print('sides', b1.get_sides())
    #b1.set_color(4,4,5,6)
    print(b1.get_color())
    b1.set_color(-1,3,5)
    print(b1.get_color())
    #b1.set_color(1)
    print(b1.get_color())
    s1 = Cube((20,30,40), 9)
    print("обьем куба:", s1.get_volume())
    print(s1.get_sides())
    s1.set_sides(1,2,3,4,5,6,7,8,9,10,11,12)
    print("nnm",s1.get_sides())
    b1.set_sides(4, 7, 678)
    print('b1 sides', b1.get_sides())
    print(b1.get_square())
    print("обьем куба:", s1.get_volume())
    s3 = Cube((3,4,4),5,6,7)
    print('s3 = ', s3.get_sides())
    s3.set_color(5,6,7)
    print(s3.get_color())
    s3.set_color(-1,-2,567)
    print(s3.get_color())
    print(a1.get_color(),'--', a1.get_sides(), ' --- ', a1.__len__())
    print(s3.__len__())'''

   circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
   cube1 = Cube((222, 35, 130), 6)

   # Проверка на изменение цветов:
   circle1.set_color(55, 66, 77)  # Изменится
   print(circle1.get_color())
   cube1.set_color(300, 70, 15)  # Не изменится
   print(cube1.get_color())

   # Проверка на изменение сторон:
   cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
   print(cube1.get_sides())
   circle1.set_sides(15)  # Изменится
   print(circle1.get_sides())

   # Проверка периметра (круга), это и есть длина:
   print(len(circle1))

   # Проверка объёма (куба):
   print(cube1.get_volume())


