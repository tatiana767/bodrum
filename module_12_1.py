"""Задача "Проверка на выносливость":
В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.

Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
test_walk - метод, в котором создаётся объект класса Runner с произвольным именем.
Далее вызовите метод walk у этого объекта 10 раз.
После чего методом assertEqual сравните distance этого объекта со значением 50.
test_run - метод, в котором создаётся объект класса Runner с произвольным именем.

Далее вызовите метод run у этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами.
Далее 10 раз у объектов вызываются методы run и walk соответственно.
Т.к. дистанции должны быть разными, используйте метод assertNotEqual,
 чтобы убедится в неравенстве результатов.
Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверку."""






import Runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        Obj = Runner.Runner("urij")
        for i in range(0,10):
            Obj.walk()
        self.assertEqual(Obj.distance, 50)

    def test_run(self):
        Obj2 = Runner.Runner('Georgij')
        for i in range(0, 10):
            Obj2.run()
        self.assertEqual(Obj2.distance, 100)

    def test_challenge(self):
         Obj3 = Runner.Runner('Vahtang')
         Obj4 = Runner.Runner('Ozzi')
         for i in range(0, 10):
            Obj3.run()
            Obj4.walk()
         self.assertNotEqual(Obj4.distance,Obj3.distance )


if __name__ == "__main__":
    unittest.main()





