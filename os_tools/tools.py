import os
import shutil
import platform

"""
создание папки
"""


def create_dir():
    dir_name = input('   Введите имя папки: ')
    if not os.path.exists(dir_name):
        # сздать папку передаем путь
        os.mkdir(dir_name)


"""
удаление файла(папки)
"""


def del_dir():
    # print(os.getcwd())
    dir_name = input('   Введите имя папки или файла : ')
    path = os.path.join(os.getcwd(), dir_name)
    # print('path=',path)
    if os.path.exists(path):
        if os.path.isfile(dir_name):
            os.remove(dir_name)
        else:
            os.rmdir(dir_name)
    else:
        print('      Файл или папка отсутсвует')


"""
копировать (файл/папку)
"""


def copy_dir():
    # print(os.getcwd())
    dir_name = input('   Введите имя папки или файла: ')
    dir_new = input('   Введите новое имя папки или файла: ')
    if os.path.exists(dir_name):
        if os.path.isfile(dir_name):
            shutil.copy(dir_name, dir_new)
        else:
            shutil.copytree(dir_name, dir_new, False, None)
    else:
        print('      Файл или папка отсутсвует')


def info_dir(type):
    # print(os.listdir())
    dir_items = os.listdir()
    for item in dir_items:
        # print('os.path.isfile(item)=',os.path.isfile(item))
        if type == 'files' and os.path.isfile(item):
            print('      ', item)
        elif type == 'dirs' and not (os.path.isfile(item)):
            print('      ', item)
        elif type == 'all':
            print('      ', item)


def info_os():
    print('      ', platform.platform())

def about():
    print('      ', '(c) Konstantin Voloshenko')
"""
смена рабочей директории
"""
def chenge_dir():
    print(os.getcwd())
    dir_name = input('   Введите новой робочей директории: ')
    if os.path.exists(dir_name):
        os.chdir(dir_name)
        print(os.getcwd())
    else:
        print('      Папка отсутсвует')

if __name__ == '__main__':
    # del_dir()
    # copy_dir()
    # info_dir('dirs')
    chenge_dir()
