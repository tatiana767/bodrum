
import Runner1 as Runner
import unittest
import logging
from logging.handlers import RotatingFileHandler

class RunnerTest(unittest.TestCase):

    #  is_frozen = False

    #@unittest.skipIf( is_frozen == True, 'Tесты в этом кейсе заморожены')

    def test_walk(self):
        try:
            Obj = Runner.Runner('vjhkb,j', -4)
            logging.info('Успешно')
            print('Succerss')
            for i in range(0,10):
                 Obj.walk()
            self.assertEqual(Obj.distance, 50)
        except ValueError as err :
            logging.warning('Неверная скорость для Runner')
        #except TypeError as err :
           # logging.warning('Неверный тип имени для Runner')

    #@unittest.skipIf( is_frozen == True, 'Tесты в этом кейсе заморожены')
    def test_run(self):
        try:
            Obj2 = Runner.Runner(455, 3 )
            logging.info('Успешно')
            for i in range(0, 10):
                Obj2.run()
            self.assertEqual(Obj2.distance, 100)
        except TypeError as err:
             logging.warning('Неверный тип имени для Runner')

    #@unittest.skipIf( is_frozen == True, 'Tесты в этом кейсе заморожены')
    def test_challenge(self):
         Obj3 = Runner.Runner('Vahtang', 3)
         Obj4 = Runner.Runner('Ozzi', 2)
         for i in range(0, 10):
            Obj3.run()
            Obj4.walk()
         self.assertNotEqual(Obj4.distance,Obj3.distance )

    logging.basicConfig(level=logging.INFO, filemode='w',
                        filename='runner_test.log',
                        format='%(levelname)s | %(asctime)s | %(message)s', encoding='utf-8')


if __name__ == "__main__":
    unittest.main()
