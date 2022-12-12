from random import sample, randint
import numpy as np


def barrel(n):
    '''
    бочонки (1 - 90)
    :return: n бочонков
    '''

    bar = [(i+1) for i in range(90)]
    bag = sample(bar, n)
    return  bag

def card():
    print('-' * 27)
    for i in range(3):
        if bool(randint(0, 1)):
            print(' * '*9)
    print('-' * 27)

# card()
# print(bool(randint(0,1)))

# index_ = [i for i in range(9)]
# indx_ = sample(index_, 5)
# print(indx_)
#
# pattern = [1 if i in indx_ else ' ' for i in range(9)]
# print(pattern)

ex = barrel(15)
print(ex)
