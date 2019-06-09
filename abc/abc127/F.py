import math
import bisect
from functools import reduce
from collections import deque

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

q = int(input())

aaa = []
len_aaa = 0
summ_diff = 0
summ_b = 0
min_x = 0
min_fx = 0
index_min_x=0
def update(a, b):
    global len_aaa
    global summ_b
    global min_x
    global min_fx
    global index_min_x
    global summ_diff



    bisect.insort_left(aaa, a)
    len_aaa += 1
    if len_aaa & 2 == 0:
        new_index_min_x = len_aaa//2 - 1
    else:
        new_index_min_x = len_aaa//2

    new_min_x = aaa[new_index_min_x]

    min_x_change = new_min_x - min_x

    summ_diff += abs(a - min_x)

    if len_aaa == 1:
        summ_diff = 0
    elif min_x_change > 0:
        summ_diff += ((new_index_min_x*2 - len_aaa)*min_x_change)
    else:
        summ_diff -= ((2*new_index_min_x - len_aaa + 2)*min_x_change)

    summ_b += b
    min_x = new_min_x
    index_min_x = new_index_min_x

    #print(index_min_x, min_x, min_x_change, summ_diff, summ_b)
    

def get_min_x():
    #print(str(min_x) + " " + str(f(min_x)))
    print(min_x, summ_diff+summ_b)

for i in range(q):
    s = input()

    #if s.startswith("1"):
    if s[0] == "1":
        a,b = map(int, s[2:].split(" "))
        update(a, b)
    else:
        get_min_x()
