import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    X = []
    for i in range(n):
        t,l,r = INTS()
        # 全部半開区間にする
        if t==1:
            r+=0.1
        elif t==2:
            pass
        elif t==3:
            l+=0.1
            r+=0.1
        elif t==4:
            l+=0.1
        X.append((l,r))

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            a = X[i]
            b = X[j]

            if a[0] < b[1] and a[1] > b[0]:
                ans += 1

    print(ans)

main()
