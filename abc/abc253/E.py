import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

class CumulativeSum():
    def __init__(self, array, key=lambda a: a, operation=lambda a,b: a+b):
        n = len(array)
        self.array = [0] * (n+1)
        for i,a in enumerate(array):
            self.array[i+1] = operation(self.array[i],key(a))

    def get(self, l, r):
        """
        指定した区間の合計を計算します。
        区間は、元の配列に対する半開区間 `[l:r)` になります。
        """
        return self.array[r] - self.array[l]

def main():
    MOD = 998244353

    n, m, k = INTS()

    # dp[i][j] = 整数をi個並べた数列で、最後の項がjであるような、問題の条件を満たす数列の個数
    dp = [ [0]*(m+1) for _ in range(n+1) ]

    for j in range(1, m+1):
        dp[1][j] = 1
    
    for i in range(2, n+1):
        # 前の行の累積和
        ruiseki = CumulativeSum(dp[i-1])
        # log(ruiseki.array)

        for j in range(1, m+1):
            if k > 0:
                dp[i][j] = (ruiseki.get(1, m+1) - ruiseki.get(max(1, j-k+1), min(m+1, j+k))) % MOD
            else:
                dp[i][j] = ruiseki.get(1, m+1) % MOD
    
    # log(dp)
    print(sum(dp[n]) % MOD)

main()
