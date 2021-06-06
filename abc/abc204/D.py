import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n = INT()
    T = INTS()
    tsum = sum(T)

    # dp[i][j] i個まで考えた状態で、オーブンAをj分にできるか？
    dp = [ [False] * (100001) for _ in range(n+1) ]

    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(100001):
            if dp[i-1][j]:
                dp[i][j] = True
            if j >= T[i-1] and dp[i-1][j - T[i-1]]:
                dp[i][j] = True
    
    ans = INF

    for j in range(100001):
        if dp[n][j]:
            x = max(j, tsum-j)
            ans = min(ans, x)

    print(ans)

main()
