from Card import Card

card_ = Card()

lst = card_.get_card()

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

    def fight(self):
        check = self.barrel(1)[0]
        print(f'Выпало: {check}\n')




        computer, status_pc = self.recognition(check, self.computer)
        user, status_user = self.recognition(check, self.user)

        # if status_pc:
        #     print('PC зачеркнул')
        # else:
        #     print('У PC ничего нет')
        #
        # if status_user:
        #     us = input('У вас есть? Д/Н\n')
        #     if us.upper() != 'Д':
        #         print('Проиграл!!!')
        # else:
        #     us = input('У вас есть? Д/Н\n')
        #     if us.upper() != 'Н':
        #         print('Проиграл!!!')



        self.show_card(computer)
        print(status_pc)
        print()

        self.show_card(user)
        print(status_user)

        return status_pc, status_user

        # if status1:
        #     print('PC зачеркнул')
        # else:
        #     print('У PC ничего нет')
        #
        # if status2:
        #     us = input('У вас есть? Д/Н\n')
        #     if us.upper() != 'Д':
        #         print('Проиграл!!!')
        # else:
        #     us = input('У вас есть? Д/Н\n')
        #     if us.upper() != 'Н':
        #         print('Проиграл!!!')





if __name__=='__main__':

    card_ = Card()
    computer = card_.get_card()
    user = card_.get_card()
    play = Play(computer, user)

    st = False


    while st != True:
        status_pc, status_user = play.fight()
        if status_pc:
            st = True
            print('Победил PC')
        if status_user:
            st = True
            print('Победил user')


    # play.fight()

















