'''Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
'''



data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(*argv):
    global res

    for i in argv:

        if isinstance(i,list):
            calculate_structure_sum(*i, )
        elif isinstance(i, tuple):
            calculate_structure_sum(*i)
        elif isinstance(i, dict):
            calculate_structure_sum(*i.items())
        elif isinstance(i, set):
            calculate_structure_sum(*i)
        elif isinstance(i, str):
            res = res + len(i)

        elif isinstance(i, int):
            res = res + i

    return res

res = 0
print('result :' ,calculate_structure_sum(*data_structure))

