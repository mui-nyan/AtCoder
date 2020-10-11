import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    h,w = get_nums_l()
    is_wall = []
    is_wall.append([True] * (w+2))
    for _ in range(h):
        is_wall.append([True] + [ c=="#" for c in input()] + [True])
    is_wall.append([True] * (w+2))

    # log(is_wall)

    # 4方向の最寄りの散らかりマスまでの距離-1を事前に求める
    dis_t = [ [0] * (w+2) for _ in range(h+2) ]
    dis_r = [ [0] * (w+2) for _ in range(h+2) ]
    dis_b = [ [0] * (w+2) for _ in range(h+2) ]
    dis_l = [ [0] * (w+2) for _ in range(h+2) ]
    # 左から右
    last = 0
    for y in range(h+2):
        for x in range(w+2):
            if is_wall[y][x]:
                last = x
            else:
                dis_l[y][x] = x - last - 1
    # 右から左
    last = 0
    for y in range(h+2):
        for x in range(w+1, -1, -1):
            if is_wall[y][x]:
                last = x
            else:
                dis_r[y][x] = last - x - 1
    # 上から下
    last = 0
    for x in range(w+2):
        for y in range(h+2):
            if is_wall[y][x]:
                last = y
            else:
                dis_t[y][x] = y - last - 1
    # 下から上
    last = 0
    for x in range(w+2):
        for y in range(h+1, -1, -1):
            if is_wall[y][x]:
                last = y
            else:
                dis_b[y][x] = last - y - 1

    n_white = sum([is_wall[y].count(False) for y in range(h+2)])

    # log(dis_l)
    # log(n_white)

    ans = 0

    # POW2 = [1] * (5000)
    # for i in range(1,5000):
    #     POW2[i] = (POW2[i-1] * 2) % MOD

    pow2memo = {}

    def pow2(n):
        if n in pow2memo:
            return pow2memo[n]
        pow2memo[n] = pow(2, n, MOD)
        return pow2memo[n]

    for y in range(h+2):
        for x in range(w+2):
            if not is_wall[y][x]:
                # このマスを照らせるマスの数
                # 4方向の最寄りの散らかりマスまでの距離-1の和 + 1
                dis = dis_t[y][x] + dis_r[y][x] + dis_b[y][x] + dis_l[y][x] + 1

                # このマスと独立なマスの数
                other = n_white - dis

                # このマスを照らす方法の数
                light = pow2(dis) - 1

                # 独立なマスを照らす方法の数
                other2 = pow2(other)

                ans = (ans + light * other2) % MOD

    print(ans)


main()
