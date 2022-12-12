from random import sample, randint



def barrel(n):
    '''
    бочонки (1 - 90)
    :return: n бочонков
    '''

    bar = [(i + 1) for i in range(90)]
    bag = sample(bar, n)
    return bag
def random_index():
    '''
    :return: 5 случайных индексов
    '''
    index_ = [i for i in range(9)]
    index_list = sample(index_, 5)
    return index_list
def create_string(gen_1):
    '''
    Формирует  lst из 5 чисел и 4 None.
    :return: lst
    '''
    temp_index = random_index()
    lst = [next(gen_1) if i in temp_index else ' ' for i in range(9)]
    return lst
def card():
    '''
    Создаем 3 строки (списка) по 9 значений для card
    Необходима функция create_string
    :return: list_1, list_2, list_3
    '''
    temp = barrel(15)  # получили 15 бочонков из мешка
    gen_1 = (i for i in temp)

    list_1 = create_string(gen_1)
    list_2 = create_string(gen_1)
    list_3 = create_string(gen_1)

    return list_1, list_2, list_3
def convert_str(arg):
    '''
    Переводит список в строку + добавляет одинаковую длину.
    :param arg: список 1
    :return: строка 1
    '''
    b = [str(i) for i in arg]
    b1 = [(i + ' ') if len(i) < 2 else i for i in b]
    s = ' '.join(b1)
    s = f'| {s} |'
    return s
def show_card(s1, s2, s3):
    '''
    Для красивого отображения card,
    нужна функция "convert_card"
    :param convert_str:
    :return: показывает card
    '''
    str1 = convert_str(s1)
    str2 = convert_str(s2)
    str3 = convert_str(s3)

    print('-' * 30)
    print(str1)
    print(str2)
    print(str3)
    print('-' * 30)



s1, s2, s3 = card()
show_card(s1, s2, s3)