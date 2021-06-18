import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

class PermutationsAndCombinations():
    def __init__(self, max=500000, mod=10**9+7):
        self.max = max
        self.mod = mod
        self.kaijo = self.init_kaijo(max, mod)

    def init_kaijo(self, MAX, MOD):
        kaijo = [0] * MAX
        kaijo[0] = 1
        for i in range(1, len(kaijo)):
            kaijo[i] = kaijo[i-1] * i % MOD
        return kaijo

    def inv(self, x):
        return pow(x, self.mod-2, self.mod)

    def nPk(self, n, k):
        return self.kaijo[n] * self.inv(self.kaijo[n-k]) % self.mod

    def nCk(self, n, k):
        return self.nPk(n,k) * self.inv(self.kaijo[k]) % self.mod

    def nHk(self, n, k):
        return self.nCk(n+k-1, k)

def main():
    MOD = 10**9+7
    n = INT()

    perm = PermutationsAndCombinations()
    nCk = perm.nCk

    for k in range(1,n+1):
        x = 0
        for a in range(1, (n+k-1) // k + 1):
            # log(n,k,a)
            x = (x + nCk(n - (k-1)*(a-1), a)) % MOD
        print(x)

main()
