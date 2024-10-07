"""Изменения в классе Runner:
Появился атрибут speed для определения скорости бегуна.
Метод __eq__ для сравнивания имён бегунов.
Переопределены методы run и walk, теперь изменение дистанции зависит от скорости.
Класс Tournament представляет собой класс соревнований, где есть дистанция, которую нужно пробежать и список участников. Также присутствует метод start, который реализует логику бега по предложенной дистанции.

Напишите класс TournamentTest, наследованный от TestCase. В нём реализуйте следующие методы:

setUpClass - метод, где создаётся атрибут класса all_results. Это словарь в который будут сохраняться результаты всех тестов.
setUp - метод, где создаются 3 объекта:
Бегун по имени Усэйн, со скоростью 10.
Бегун по имени Андрей, со скоростью 9.
Бегун по имени Ник, со скоростью 3.
tearDownClass - метод, где выводятся all_results по очереди в столбец.

Так же методы тестирования забегов, в которых создаётся объект Tournament на дистанцию 90.
У объекта класса Tournament запускается метод start, который возвращает словарь в переменную all_results.
В конце вызывается метод assertTrue, в котором сравниваются последний объект из
 all_results (брать по наибольшему ключу) и предполагаемое имя последнего бегуна.
Напишите 3 таких метода, где в забегах участвуют (порядок передачи в объект Tournament соблюсти):
Усэйн и Ник
Андрей и Ник
Усэйн, Андрей и Ник.
Как можно понять: Ник всегда должен быть последним.
"""



import Runner
import unittest
import pprint

class TournamentTest(unittest.TestCase):

    is_frozen = True
    #self.run1 = Runner.Runner('Uain')
    def SetUp(self):

        self.run1 = Runner.Runner('Uain', 10)
        self.run2 = Runner.Runner('Andrey', 9)
        self.run3 = Runner.Runner('Nik', 3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.res = []

    def testRun1(self):
         self.run1 = Runner.Runner('Uain', 10)
         self.run2 = Runner.Runner('Andrey', 9)
         self.run3 = Runner.Runner('Nik', 3)
         obj = Runner.Tournament(90, self.run1, self.run3)
         TournamentTest.all_results = obj.start()
         TournamentTest.res.append(TournamentTest.all_results)

         print('RUN#1', TournamentTest.all_results[max(TournamentTest.all_results.keys())])
         self.assertTrue(self.all_results[max(self.all_results.keys())], 'Nik')

    def testRun2(self):

        self.run1 = Runner.Runner('Uain', 10)
        self.run2 = Runner.Runner('Andrey', 9)
        self.run3 = Runner.Runner('Nik', 3)
        obj = Runner.Tournament(90, self.run2, self.run3)
        TournamentTest.all_results = obj.start()
        TournamentTest.res.append(TournamentTest.all_results)

        print('RUN#2', TournamentTest.all_results[max(TournamentTest.all_results.keys())])
        self.assertTrue(self.all_results[max(self.all_results.keys())], 'Nik')

    def testRun3(self):

        self.run1 = Runner.Runner('Uain', 10)
        self.run2 = Runner.Runner('Andrey', 9)
        self.run3 = Runner.Runner('Nik', 3)
        obj = Runner.Tournament(90, self.run1, self.run2, self.run3)
        TournamentTest.all_results = obj.start()
        TournamentTest.res.append(TournamentTest.all_results)

        print('RUN#3', TournamentTest.all_results[max(TournamentTest.all_results.keys())])
        self.assertTrue(self.all_results[max(self.all_results.keys())], 'Nik')


        #print("!",obj.start())



    @classmethod
    def tearDownClass(cls):

        j = 1
        for i in TournamentTest.res:
            print(f'забег {j}:')
            j+=1
            for key, value in i.items():
                print(key, "-" , value)





if __name__ == "__main__":
    unittest.main()
