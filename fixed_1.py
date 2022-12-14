from Card import Card
import copy

# card_ = Card()
#
# lst = card_.get_card()

class Play(Card):

    def __init__(self, computer, user):

        self.computer = computer
        self.user = user

    def happy_end(self, lst):
        '''
        Проверяет остались ли в карточке незакрашенные значения!!!
        :param lst: принимает карточку
        :return: bool
        '''
        for s in lst:
            for n in s:
                if type(n) != str:
                    return False
        return True

    def recognition(self, check, lst):
        status = False
        for s in range(len(lst)):
            if check in lst[s]:
                indx = lst[s].index(check)
                lst[s][indx] = 'X'
                status = True
        return lst, status

    def fight_manually(self):
        check = self.barrel(1)[0]

        print(f'Выпало: {check}\n')

        user1 = copy.deepcopy(self.user)


        computer, status_pc = self.recognition(check, self.computer)
        user, status_user = self.recognition(check, self.user)

        # self.show_card(computer)
        # self.show_card(user)

        if status_pc:
            print('PC зачеркнул')
            self.show_card(computer)
            print()
        else:
            print('У PC ничего нет')
            self.show_card(computer)
            print()

        if status_user:
            self.show_card(user1)
            us = input('У вас есть? Д/Н\n')
            if us.upper() != 'Д':
                print('Проиграл!!!')


        else:
            self.show_card(user1)
            us = input('У вас есть? Д/Н\n')
            if us.upper() != 'Н':
                print('Проиграл!!!')





        return computer, status_pc, user, status_user

    def fight_auto(self):
        check = self.barrel(1)[0]

        print(f'Выпало: {check}\n')

        user1 = copy.deepcopy(self.user)


        computer, status_pc = self.recognition(check, self.computer)
        user, status_user = self.recognition(check, self.user)

        self.show_card(computer)
        self.show_card(user)

        return computer, status_pc, user, status_user







if __name__=='__main__':

    us = input('У вас есть? Д/Н\n')
    if us.upper() != 'Д':
        print('Проиграл!!!')
















