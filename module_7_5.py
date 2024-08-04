'''
Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.'''


import os
import time

for root1, dir_, files in os.walk(os.getcwd()):

    for file in files:
        os.chdir(root1)
        filepath = os.path.join(root1)
        filetime = os.stat(file).st_mtime
        filetime1 = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        formatted_time1 = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime1))
        filesize = os.stat(file).st_mtime
        filesize1 = os.path.getmtime(file)
        parent_dir = os.path.dirname(str(os.getcwd()))
       # print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize1} байт, Время изменения: {formatted_time1}, Родительская директория: {parent_dir}')


