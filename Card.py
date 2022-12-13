from random import sample, randint


class GetCard:

    def __init__(self):
        pass


    def barrel(self, n):
        '''
        бочонки (1 - 90)
        :return: n бочонков
        '''

        bar = [(i + 1) for i in range(90)]
        bag = sample(bar, n)
        return bag

    def random_index(self):
        '''
        :return: 5 случайных индексов
        '''
        index_ = [i for i in range(9)]
        index_list = sample(index_, 5)
        return index_list

    def create_string(self):
        '''
        Формирует  lst из 5 чисел и 4 None.
        :return: lst
        '''
        temp = self.barrel(15)
        self.gen_1 = (i for i in temp)

        temp_index = self.random_index()
        lst = [next(self.gen_1) if i in temp_index else ' ' for i in range(9)]
        return lst

    def card(self):
        '''
        Создаем 3 строки (списка) по 9 значений для card
        Необходима функция create_string
        :return: list_1, list_2, list_3
        '''
        self.list_1 = self.create_string()
        self.list_2 = self.create_string()
        self.list_3 = self.create_string()

        return self.list_1, self.list_2, self.list_3

    def convert_str(self, arg):
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


    def show_card(self):
        '''
        Для красивого отображения card,
        нужна функция "convert_card"
        :param convert_str:
        :return: показывает card
        '''
        str1 = self.convert_str(self.list_1)
        str2 = self.convert_str(self.list_2)
        str3 = self.convert_str(self.list_3)

        print('-' * 30)
        print(str1)
        print(str2)
        print(str3)
        print('-' * 30)


card_ = GetCard()

a,b,c = card_.card()
print(a, b, c, sep='\n')

card_.show_card()