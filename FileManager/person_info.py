#Год рожденя случайного человека из словоря

import random

def random_person():

        #словарь известных людей
        answer_dict = {
                'picasso': '25.10.1881',
                'repin': '05.08.1844',
                'magellan': '20.10.1480',
                'einstein': '18.04.1955',
                'newton': '04.01.1643',
                'mozart': '27.01.1756',
                'pushkin': '06.05.1799',
                'mikilanjilo': '27.01.1756',
            }
        #Выбираем случайного человека из словаря
        name, date = random.choice(list(answer_dict.items()))
        return name, date


name, date = random_person()

print(name, date)
