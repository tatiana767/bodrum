'''Выполнение:
Создайте функцию read_info(name), где name - название файла. Функция должна:
Создавать локальный список all_data.
Открывать файл name для чтения.
Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
Во время считывания добавлять каждую строку в список all_data.
Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного
выполнения программы над линейным.
Создайте список названий файлов в соответствии с названиями файлов архива.
Вызовите функцию read_info для каждого файла по очереди (линейно) и
измерьте время выполнения и выведите его в консоль.
Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
 контекстный менеджер with и объект Pool. Для вызова функции используйте метод map,
  передав в него функцию read_info и список названий файлов. Измерьте время выполнения и выведите его в консоль.
Для избежания некорректного вывода запускайте линейный вызов и многопроцессный по отдельности,
предварительно закомментировав другой.'''
import multiprocessing

from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file :
        str_ = file.readline()
        if str_!='':
            all_data.append(str_)



filenames_ = [f'./111/file {number}.txt' for number in range(1, 5)]

start = datetime.now()
for i in filenames_:
       #print(i)
       read_info(i)
end = datetime.now()
print('--', end - start)


'''if __name__=='__main__':


    all_files = [f'./111/file {number}.txt' for number in range(1, 5)]
    start = datetime.now()
    with multiprocessing.Pool(processes=3) as pool:
            pool.map(read_info, all_files)

    end = datetime.now()
    print(end - start)'''




