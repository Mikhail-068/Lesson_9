from Card import Card
from fixed_1 import Play

card_ = Card()

computer = card_.get_card()
user = card_.get_card()

play = Play(computer, user)

ex1 = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]


for i in range(9):
       ex1, _ = play.recognition(i, ex1)

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



a = hapy_end(ex1)
print(a)