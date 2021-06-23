import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, k = INTS()
    A = INTS()
    B = INTS()

    diff = 0
    for a,b in zip(A,B):
        diff += abs(a-b)

    print("Yes" if diff <= k and (k-diff)%2==0 else "No")

main()
