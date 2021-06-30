import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    MOD = 10**9+7

    n, l = INTS()
    # dp[i] = i段登る方法の数
    dp = [0] * (n+1)
    dp[0] = 1

    for i in range(n):
        dp[i+1] = dp[i] + (0 if i+1<l else dp[i+1-l])
        dp[i+1] %= MOD

    print(dp[n])

main()
