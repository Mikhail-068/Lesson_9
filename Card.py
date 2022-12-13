from random import sample, randint


class Card:

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

    def get_card(self):
        '''
        Создаем 3 строки (списка) по 9 значений для card
        Необходима функция create_string
        :return: list_1, list_2, list_3
        '''
        all_list = []
        for i in range(3):
            all_list.append(self.create_string())

        return all_list

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

    def show_card(self, lst):
        '''
        Для красивого отображения card,
        нужна функция "convert_card"
        :param convert_str:
        :return: показывает card
        '''
        print('-' * 30)
        for i in range(3):
            print(self.convert_str(lst[i]))
        print('-' * 30)



if __name__=='__main__':
    card_ = Card()

    lst = card_.get_card()

    card_.show_card(lst)
    print(lst)