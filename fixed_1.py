from Card import Card

card_ = Card()

lst = card_.get_card()

class Play(Card):

    def __init__(self, computer, user):
        self.computer = computer
        self.user = user


    def show_1(self):
        print(self.computer)

    def recognition(self, check, lst):
        status = False
        for s in range(len(lst)):
            if check in lst[s]:
                indx = lst[s].index(check)
                lst[s][indx] = 'X'
                status = True
        return lst, status

    def fight(self):
        check = self.barrel(1)
        print(f'Выпало: {check}\n')



        comp, status_pc = self.recognition(check, self.computer)
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



        self.show_card(comp)
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

    st = False

    while st != True:
        # play = Play(computer, user)
        # status1, status2 = play.fight()
        # if status1: st = True
        # if status2: st = True

        play.recognition(16, )















