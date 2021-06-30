import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, k = INTS()
    P = []
    for i in range(n):
        a,b = INTS()
        a = a-b
        P.append(a)
        P.append(b)
    P.sort(reverse=True)
    print(sum(P[:k]))

main()
