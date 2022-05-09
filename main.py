import os_tools.tools as f
import bank.bank as b
import victory.victory as v
"""
Консольный файловый менеджер
"""
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню : ')
    if choice == '1':
        f.create_dir()
    elif choice == '2':
        f.del_dir()
    elif choice == '3':
        f.copy_dir()
    elif choice == '4':
        f.info_dir('all')
    elif choice == '5':
        f.info_dir('dirs')
    elif choice == '6':
        f.info_dir('files')
    elif choice == '7':
        f.info_os()
    elif choice == '8':
        f.about()
    elif choice == '9':
        v.run()
    elif choice == '10':
        b.run()
    elif choice == '11':
        f.chenge_dir()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
