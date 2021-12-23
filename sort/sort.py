from typing import List
from random import shuffle, randint
from time import sleep


def __is_sorted__(l: List[int]) ->bool:
    '''
    check the input list is sorted
    '''
    return all(a <= b for a, b in zip(l, l[1:]))


def bogo_sort(l: List[int]) -> List[int]:
    '''
    bogo sort:  https://en.wikipedia.org/wiki/Bogosort
    The time complexity depends on the user.
    Only for @SNURFER the time complexity is O(1), not guaranteed for others.
    '''
    while not __is_sorted__(l):
        shuffle(l)
    return l


def slow_sort(l: List[int], i: int, j: int) -> None:
    '''
    slow sort: https://en.wikipedia.org/wiki/Slowsort
    '''
    if i >= j:
        return
    m = (i + j) // 2
    slow_sort(l, i, m)
    slow_sort(l, m + 1, j)
    if l[m] > l[j]:
        l[m], l[j] = l[j], l[m]
    slow_sort(i, i, j - 1)


def tmax_sort(l: List[int]) -> None:
    raise NotImplementedError('설계 면담 중 입니다.')


def pk_sort(l: List[int]) -> None:
    raise NotImplementedError('있다치고')


def ux_sort(l: List[int]) -> None:
    raise NotImplementedError('가이드가 나오지 않았습니다.')


def random_sort(l: List[int]) -> None:
    num = randint(0, 9)
    if num == 1:
        bogo_sort(l)
    elif num == 2:
        slow_sort(l, 0, len(l) - 1)
    elif num == 3:
        tmax_sort(l)
    elif num == 4:
        pk_sort(l)
    elif num == 5:
        ux_sort(l)
    else:
        while(1):
            sleep(1)
            print('담당자가 퇴사 했습니다.')
