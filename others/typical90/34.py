from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, k = INTS()
    A = INTS()

    count = defaultdict(int)

    tail = 0
    head = 0

    ans = 0
    while head < n:
        count[A[head]] += 1

        if len(count) <= k:
            if head - tail + 1 > ans:
                ans = head - tail + 1

        while len(count) > k:
            count[A[tail]] -= 1
            if count[A[tail]] == 0:
                del count[A[tail]]
            tail += 1

        head += 1

    print(ans)

main()
