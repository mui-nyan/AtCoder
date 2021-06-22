import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    INF = 2**31-1

    n = INT()
    a,b,c = INTS()
    a,b,c = sorted((a,b,c), reverse=True)

    ans = INF
    for i in range(10000):
        if i*a > n:
            break
        for j in range(10000-i):
            if i*a + j*b > n:
                break
            x = n - (i*a) - (j*b)
            if x % c == 0:
                k = x//c
                ans = min(ans, i+j+k)

    print(ans)

main()
