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
import os
print('1. создать папку;')
print('2.  удалить (файл/папку);')
print('3. копировать (файл/папку);')
print('4. просмотр содержимого рабочей директории;')
print('5. сохранить содержимое рабочей директории в файл;')
print('6. посмотреть только файлы;')
print('7. просмотр информации об операционной системе;')
print('8. создатель программы;')
print('9. играть в викторину;')
print('10. мой банковский счет;')
print('11. выход.')


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

elif choice == '5':
    with open('listdir.txt', 'w') as f:
        foldirs = [e for e in os.listdir() if os.path.isdir(e)]
        f.write(f'dirs: {foldirs} \n')
    with open('listdir.txt', 'a') as f:
        filename = [e for e in os.listdir() if os.path.isfile(e)]
        f.write(f'files: {filename} , ')

elif choice == '6':
    print(os.listdir())

elif choice == '7':
    print(platform.platform())

elif choice == '8':
    print(sys.version_info)

elif choice == '9':
    rounds = int(input('Сколько раз вы хотите играть?'))
    #for i in range(rounds):
        #person_and_question()
    rounds = [person_and_question() for i in range(rounds)]

    print('Пока')

elif choice == '10':
    my_account = 0
    checklist = []
    my_accounts = []
    if os.path.exists('cheklist.txt'):
        with open('cheklist.txt', 'r') as f:
            result=[checklist.append(names.replace('\n', ''))for names in f]
            #for names in f:
                #checklist.append(names.replace('\n', ''))

    while True:
        try:


            print('1. пополнение счета')
            print('2. покупка')
            print('3. история покупок')
            print('4. выход')
            print(f'Ваш счет {my_account}')

            choice = int(input('Выберите пункт меню'))
            if choice == '1':
                sum = int(input('Введите сумму'))
                my_account += sum
                my_accounts.append(sum)

            elif choice == '2':
                sum = int(input('Введите сумму покупки'))
                if sum > my_account:
                    print('На счету недостаточно средств')
                else:
                    my_account -= sum
                    name = input('Введите название покупки')
                    checklist.append(name)

            elif choice == '3':
                print('История покупок: ', checklist)
            elif choice == '4':
                with open('sum.txt', 'w') as f:
                    result=[ f.write(f'{my_account}\n')for sum in my_accounts]
                    #for sum in my_accounts:
                        #f.write(f'{my_account}\n')
                with open('cheklist.txt', 'w') as f:
                    reult=[ f.write(f'{name}\n')for name in checklist]
                    #for name in checklist:
                        #f.write(f'{name}\n')
        except:
            print('Введите число пожалуйста от 1 до 4')


elif choice == '11':
   sys.exit()




