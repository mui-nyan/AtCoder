import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, q = INTS()
    A = INTS()

    shift = 0

    for _ in range(q):
        t,x,y = INTS()

        x = (x-shift-1)%n
        y = (y-shift-1)%n

        if t == 1:
            A[x], A[y] = A[y], A[x]
        elif t == 2:
            shift += 1
            shift %= n
        else:
            print(A[x])

main()
