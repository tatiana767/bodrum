'''Задание "Слишком древний шифр":
Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса". (Как жаль, что они поняли это так поздно :( ).

Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.

Пример кратности(деления без остатка):
1 + 2 = 3 (сумма пары)
9 / 3 = 3 (ровно 3 без остатка)
9 кратно 3 (9 делится на 3 без остатка)


Пример 1:
9 - число из первой вставки
1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

Пример 2:
11 - число из первой вставки
11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)'''

number_ = int(input('Введите число от 3 до 20: '))
list_=[]

for i in range(0, number_):
    list_.append([])

    for j in range(1,number_):

        if i > 0 and number_%(i+j) == 0:
            list_[i].append([i, j])

list_.pop([0][0])

print(list_)
def s_(n, m):
    if m!=n:
        for j in range(0, len(list_[m - 1])):
            if j < len(list_[m-1]):
                #print(list_[m - 1][j])
                print(f'm : {m} n: {n}  j= {list_[m - 1][j][1]}')
                if list_[m - 1][j][1] == n:
                    #print('sfsgsdg: ', list_[m - 1][j], j)
                    #print(f'{list_[m - 1][j][1]} == n:{n}')
                    print('delete:', list_[m - 1].pop(j))
                    if len(list_[m-1]) == 0 :
                        #print('!!!')
                        list_.pop(m-1)
                    print('control :', list_)
                    break


for i in range(0, len(list_)):
   if i < len(list_):
        #print("i = ", i , 'len[i] = ', len(list_[i]))
        for j in range(0, len(list_[i])):
            #print('j= ', j )
            if i == j:
                continue
            else :
                #print(f'(вызываем для {list_[i][j][0]} - {list_[i][j][1]}')
                s_(list_[i][j][0],list_[i][j][1])

print('итоговый список : ', list_)





