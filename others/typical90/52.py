import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    MOD = 10**9+7
    n = INT()
    ans = 1
    for _ in range(n):
        x = sum(INTS()) % MOD
        ans *= x
        ans %= MOD
    print(ans)
main()
