'''Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.'''


def all_variants(text):

    for i in range(0, len(text)):
        for j in range(1, len(text)+1):
               if text[i:j] :
                  yield text[i:j]






for i in all_variants('abc'):
    print(i)

