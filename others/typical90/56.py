import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    n, s = INTS()

    A = []
    B = []

    for i in range(n):
        a,b = INTS()
        A.append(a)
        B.append(b)
    
    # dp[i][j] = i日目までを考慮して、合計をj円にする方法があるか？
    dp = [[False] * (s+1) for _ in range(n+1)]
    # 0日目0円は自明にOK
    dp[0][0] = True

    for i in range(1, n+1):
        for j in range(s + 1):
            # 1日前に 「j - (この商品の値段) 円」 が可能なら可能
            if A[i-1] <= j and dp[i-1][j - A[i-1]]:
                dp[i][j] = True
            if B[i-1] <= j and dp[i-1][j - B[i-1]]:
                dp[i][j] = True

    if dp[n][s] == False:
        # n日目にs円にする方法がない
        print("Impossible")
        return

    # 最終日の状態からさかのぼって、どの商品を選べばよいかを調べる
    x = n
    y = s
    ans = []
    while x > 0:
        if y >= A[x-1] and dp[x-1][y-A[x-1]]:
            ans.append("A")
            y -= A[x-1]
        elif y >= B[x-1] and dp[x-1][y-B[x-1]]:
            ans.append("B")
            y -= B[x-1]
        x -= 1

    print("".join(list(reversed(ans))))

main()
