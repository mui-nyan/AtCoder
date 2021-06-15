from bisect import bisect_right
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, q = INTS()
    A = INTS()
    # 重複排除してソート
    A = list(set(A))
    A.sort()
    for i in range(q):
        k = INT()

        left = -1
        right = 10**18+3*n
        while left+1<right:
            mid = (left+right) // 2
            # mid以下の要素数+kがmid以下である最小のmidを探す
            x = bisect_right(A, mid)
            ok = x+k <= mid

            if ok:
                right = mid
            else:
                left = mid
        print(right)

main()
