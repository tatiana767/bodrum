'''Создайте 3 класса (2 из которых будут исключениями):
Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:
__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.
__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.
'''

class Car:
  model = ''
  __vin = 0
  __numbers = ''
  def __init__(self, model, vin, numbers ):
      self.model = model
      self.__vin = vin
      self.__numbers = numbers
      self.__is_valid_vin(vin)
      self.__is_valid_numbers(numbers)


  def __is_valid_vin(self, vin_number):
    if isinstance(vin_number, int) == False:
      raise IncorrectVinNumber('Некорректный тип vin номер')

    elif vin_number < 1000000 or vin_number > 9999999 :
      raise IncorrectVinNumber('Неверный диапазон для vin номера')

    else:
      return True


  def  __is_valid_numbers(self, numbers):
    if isinstance(numbers, str) == False:
      raise IncorrectCarNumber('Некорректный тип данных для номеров', )
    elif  len(numbers) != 6 :
       raise IncorrectCarNumber('Неверная длина номера')
    else:
      return True


class IncorrectVinNumber(Exception):
   def __init__(self,message):
     self.message = message


class IncorrectCarNumber(Exception):
  def __init__(self, message):
    self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')

except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')


try:
  third = Car('Model3', 2020202, 'нет номера')

except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumber as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

