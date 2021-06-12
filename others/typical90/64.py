import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, q = INTS()
    A = INTS()

    kaisa = [0] * (n-1)
    for i in range(n-1):
        kaisa[i] = A[i+1] - A[i]

    # log(kaisa)

    fuben = sum(map(abs, kaisa))
    # log(fuben)

    for i in range(q):
        l,r,v = INTS()
        l -= 1
        r -= 1

        ly = 0
        ry = 0

        if l > 0:
            lx = kaisa[l-1] + v
            ly = abs(lx) - abs(kaisa[l-1])
            kaisa[l-1] += v

        if r < n-1:
            rx = kaisa[r] - v
            ry = abs(rx) - abs(kaisa[r])
            kaisa[r] -= v

        fuben = fuben + ly + ry
        print(fuben)

main()
