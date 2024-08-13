'''Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и "Составное" в противном случае.
'''


def is_prime(func):

    def proverka(a, b, c):
        count = 0
        res = func(a,b,c)
        for i in range(2, res):
            if res%i == 0:
                count += 1
        if count == 0:
            print(f' {a}+{b}+{c} простое')
        else :
            print(f' {a}+{b}+{c} составное')
        return count
    return proverka


@is_prime
def sum_three(a, b, c):
    return int(a+b+c)


d = sum_three(2, 4, 6)
c =  sum_three(1, 1,  1)