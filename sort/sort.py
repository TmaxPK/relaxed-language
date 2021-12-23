from typing import List
from random import shuffle


def __is_sorted__(l: List[int]) ->bool:
  '''
  check the input list is sorted
  '''
  return all(a <= b for a, b in zip(l, l[1:]))


def bogo_sort(l: List[int]) -> List[int]:
  '''
  bogo sort:  https://en.wikipedia.org/wiki/Bogosort
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
  
