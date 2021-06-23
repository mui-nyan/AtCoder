import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n = INT()
    s = input()

    # dp[i] = bがi個並んだ列に対して何回操作できるか？
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(1,n+1):
        dp[i] = dp[i-1]*2 + 1

    ans = 0

    for i in range(n):
        if s[i] == "b":
            ans += dp[i]+1
        elif s[i] == "c":
            ans += dp[i]*2+2

    print(ans)

main()
