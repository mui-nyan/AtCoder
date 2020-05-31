import sys

from statistics import median

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

n = int(input())
AB = []
for _ in range(n):
    AB.append(get_nums_l())
A = [ ab[0] for ab in AB ]
B = [ ab[1] for ab in AB ]

if n%2 == 1:
    min_of_med = median(A)
    max_of_med = median(B)
    print(max_of_med - min_of_med + 1)

else:
    A.sort()
    B.sort()
    min_of_med = A[n//2 - 1] + A[n//2]
    max_of_med = B[n//2 - 1] + B[n//2]
    print(max_of_med - min_of_med + 1)
