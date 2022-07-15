#Викторина дата рождения случайного человека из словаря

#Импортируем функции из модуля
# from <<название модуля>> import названия функций через ,
from famous_info import random_person, person_and_question

rounds = int(input('Сколько раз вы хотите играть?'))
for i in range(rounds):
    person_and_question()

print('Пока')
