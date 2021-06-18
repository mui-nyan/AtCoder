import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()

    X = []
    Y = []
    for i in range(n):
        x,y = INTS()
        X.append(x)
        Y.append(y)
    
    X.sort()
    Y.sort()

    mx = X[(n-1)//2]
    my = Y[(n-1)//2]

    ans = 0
    for x in X:
        ans += abs(mx - x)
    for y in Y:
        ans += abs(my - y)

    print(ans)

main()
