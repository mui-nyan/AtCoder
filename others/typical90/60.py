from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def LIS(L):
    # dp1[i] = 長さ(i+1)の増加部分列の末尾として考えられる最小の値
    dp1 = []
    # dp2[i] = L[i]を末尾に置いた場合の最長増加部分列
    dp2 = [0] * len(L)
    for i, ai in enumerate(L):
        pos = bisect_left(dp1, ai)
        dp2[i] = pos+1
        if len(dp1) <= pos:
            dp1.append(ai)
        else:
            dp1[pos] = ai
    return dp2

def main():
    n = INT()
    A = INTS()

    lis_l = LIS(A)
    lis_r = LIS(A[::-1])[::-1]

    ans = 0
    for i in range(n):
        x = lis_l[i] + lis_r[i] - 1
        if x > ans:
            ans = x

    print(ans)

main()
