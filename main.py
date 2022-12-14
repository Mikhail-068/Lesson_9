from Card import Card
from fixed_1 import Play

card_ = Card()

computer = card_.get_card()
user = card_.get_card()




#
# ex1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
play = Play(computer, user)


def happy_end(lst):
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



while True:
       comp, st_PC, user, st_user = play.fight_manually()
       PC = play.happy_end(comp)
       USER =  play.happy_end(user)
       if PC:
              print('Выиграл Computer...')
              play.show_card(comp)
              play.show_card(user)
              break
       if USER:
              print('Вы выиграли !!!')
              play.show_card(comp)
              play.show_card(user)
              break
