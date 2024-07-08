'''Задание "Средний балл":
Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":

На вход даны следующие данные:
Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
Например: 'Aaron' - [5, 3, 3, 5, 4]
Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

Вывод в консоль:
{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}'''

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Dict = {}

names = list(students)
print(names)

for i in range(5):
  #print(names[i][0])
  for j in range(i+1, 5):
        if names[i][0] > names[j][0] :
         # print("Yes")
         # print ("i = ", i, "j = ", j, names[i],names[j])
          value = names[i]
          names[i]=names[j]
          names[j] = value

       #else : print ("No")


print(names)

for i in range(names.__len__()):
    #print(sum(grades[i])/len(grades[i]))
    Dict.update({names[i]: sum(grades[i])/len(grades[i])})

print(Dict)






