import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    MOD = 10**9+7

    n = INT()
    s = input()

    # dp[i][j] = j文字まで考慮して、
    # "atcoder"をi文字完成させている選び方の数
    dp = [[0] * (n+1) for _ in range(7+1)]
    
    for j in range(n+1):
        dp[0][j] = 1

    for j in range(n):
        c = s[j]
        ci = "atcoder".find(c)
        ci += 1
        for i in range(1, 7 + 1):
            if i == ci:
                dp[i][j+1] = (dp[i][j] + dp[i-1][j]) % MOD
            else:
                dp[i][j+1] = dp[i][j]

    print(dp[7][n])

main()
