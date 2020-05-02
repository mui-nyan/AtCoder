import math
from functools import reduce
from collections import deque
import sys
sys.setrecursionlimit(10**7)

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

# cdef int n,k,d,prev,j,a,m,mi

class segtree:
    def __init__(self, n,operator,identity):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.num_end_leaves = 2**(len(nb)-1)
        else:
            self.num_end_leaves = 2**(len(nb))

        self.array = [identity for i in range(self.num_end_leaves * 2)]
        self.identity = identity
        self.operator =operator

    def update(self,x,val):
        actual_x = x+self.num_end_leaves
        self.array[actual_x] = val
        while actual_x > 0 :
            actual_x = actual_x//2
            self.array[actual_x] = self.operator(self.array[actual_x*2],self.array[actual_x*2+1])

    def get(self,q_left,q_right,arr_ind=1,leaf_left=0,depth=0):
        """
        [q_left, q_right] (閉区間) の値を集計して返します。
        """

        width_of_floor = self.num_end_leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if leaf_left > q_right or leaf_right < q_left:
            return  self.identity

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[arr_ind]

        else:
            val_l = self.get(q_left,q_right,2*arr_ind,leaf_left,depth+1)
            val_r = self.get(q_left,q_right,2*arr_ind+1,leaf_left+width_of_floor//2,depth+1)
            return self.operator(val_l,val_r)


n,k,d = get_nums_l()
A = get_nums_l()

sg = segtree(n, min, (99999999999999999999, 99999999999999999999))
for i,a in enumerate(A):
    sg.update(i, (a,i))

# 不可能なパターン
if n < d*(k-1)+1:
    print(-1)
    exit()

ans = []

prev = -2147000000
for i in range(1, k+1):
    m = 2147000000
    mi = -1
    # 次取れる候補
    m,mi = sg.get(max(0, prev+d), n-(k-i)*d-1)
    # for j in range(max(0, prev+d), n-(k-i)*d):
    #     a = A[j]
    #     if a < m:
    #         m = a
    #         mi = j
    ans.append(m)
    prev = mi

print(" ".join(map(str, ans)))
