import math
from functools import reduce

def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

n,k = get_nums_l()

ans = 0
for init_score in range(1,n+1):
    score = init_score
    # 勝つために連続で表を出さなければならない回数
    need = 0
    while score < k:
        need += 1
        score *= 2

    rate = 1 / 2**need
    ans += rate / n

print(ans)