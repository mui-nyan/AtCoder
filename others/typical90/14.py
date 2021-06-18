import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    A = INTS()
    B = INTS()

    A.sort()
    B.sort()

    ans = 0
    for i in range(n):
        ans += abs(A[i]-B[i])
    
    print(ans)

main()
