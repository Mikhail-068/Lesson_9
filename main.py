from random import sample


def barrel():
    '''
    бочонок => для генерации случайно
    взятого бачонка из мешка
    :return: номер бочонка в заданном диапозоне
    '''

    bar = [(i+1) for i in range(90)]
    bag = sample(bar, 1)
    return  bag

