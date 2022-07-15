'''
- создать папку;
- удалить (файл/папку);
- копировать (файл/папку);
- просмотр содержимого рабочей директории;
- посмотреть только папки;
- посмотреть только файлы;
- просмотр информации об операционной системе;
- создатель программы;
- играть в викторину;
- мой банковский счет;
- смена рабочей директории (*необязательный пункт);
- выход.
'''
import os
import shutil
import platform
import sys
from famous_info import person_and_question

print('1. создать папку;')
print('2.  удалить (файл/папку);')
print('3. копировать (файл/папку);')
print('4. просмотр содержимого рабочей директории;')
print('5. посмотреть только папки;')
print('6. посмотреть только файлы;')
print('7. просмотр информации об операционной системе;')
print('8. создатель программы;')
print('9. играть в викторину;')
print('10. мой банковский счет;')
print('11. смена рабочей директории;')
print('12. выход.')

choice = input('Выберите пункт меню')
if choice == '1':
    name = input('Введите имя папки')
    if not os.path.isdir('name'):
        os.mkdir(name)

elif choice == '2':
    name = input('Введите имя папки')
    os.rmdir(name)

elif choice == '3':
    name = input('Введите имя папки')
    name1 = input('Введите имя папки №1')
    shutil.copytree(name, name1)

elif choice == '4':
    print(os.getcwd())

elif choice == '6':
    print(os.listdir())

elif choice == '7':
    print(platform.platform())

elif choice == '8':
    print(sys.version_info)

elif choice == '9':
    rounds = int(input('Сколько раз вы хотите играть?'))
    for i in range(rounds):
        person_and_question()

    print('Пока')

elif choice == '10':
    my_account = 0
    checklist = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {my_account}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            sum = int(input('Введите сумму'))
            my_account += sum

        elif choice == '2':
            sum = int(input('Введите сумму покупки'))
            if sum > my_account:
                print('На счету недостаточно средств')
            else:
                my_account -= sum
                name = input('Введите название покупки')
                checklist.append((name, sum, my_account))

        elif choice == '3':
            print('История покупок: ', checklist)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

elif choice == '11':
    sys.exit()




