from bisect import bisect_left
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

ord_a = ord("a")
def to_ord(c):
    return ord(c) - ord_a

def main():
    n, k = INTS()
    s = input()

    # index[i] = 文字iが登場する添字の一覧
    index=[[] for _ in range(26)]
    for i,c in enumerate(s):
        index[to_ord(c)].append(i)

    ans = []
    prev = 0
    for i in range(k):
        for c in "abcdefghijklmnopqrstuvwxyz":
            ord_c = to_ord(c)
            x = bisect_left(index[ord_c], prev)
            if x < len(index[ord_c]):
                # xi = 配列のprev番目以降でcが出現する最初の添字
                xi = index[ord_c][x]
                if xi <= n - k + i:
                    ans.append(c)
                    prev = xi+1
                    break

    print("".join(ans))

main()
