import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    INF = 2**31-1
    MOD = 10**9+7

    k = INT()

    if k%9 != 0:
        print(0)
        return

    # dp[i] = 1～9をいくつか足して、その合計がiであるような組み合わせの数
    #       = 9面ダイスでiマス先に到達できる出目のパターンの数
    dp = [0] * (k+1)
    dp[0] = 1
    for i in range(k):
        for j in range(1,10):
            if i+j <= k:
                dp[i+j] = (dp[i+j]+dp[i]) % MOD

    print(dp[k])

main()
