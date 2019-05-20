# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import shutil

def make_dir (name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - такая папка уже есть'.format(name))


def remove_dir (name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - не существует'.format(name))


def start ():
    user_answer =''
    count_dirs = range(1, 10)

    while user_answer != '3':

        user_answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')

        if user_answer == '1':
            for i in count_dirs:
                i = str(i)
                make_dir('dir_' + i)
        elif user_answer == '2':
            for i in count_dirs:
                i = str(i)
                remove_dir('dir_' + i)
        elif user_answer =='3':
            break

start()


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir ():
    buffer = os.listdir()
    print('Список файлов:')
    for index, element in enumerate(buffer, start=1):
        if os.path.isdir(element):
            print('{}. {}'.format(index, element))


list_dir()


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def current_file_copy ():
    name_file = os.path.realpath(__file__)
    new_file = name_file +'.copy'
    if os.path.isfile(new_file) != True:
        shutil.copy(name_file, new_file)
        return new_file + ' - создан'
    else:
        return 'Копия текущего файла уже есть'


print(current_file_copy())
