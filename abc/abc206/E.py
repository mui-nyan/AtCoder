from functools import reduce
from itertools import combinations
import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def prime_factorize(n, factors):
    """
    素因数分解
    
    Sample:
        prime_factorize(36)
        => [2, 2, 3, 3]

        collections.Counter(prime_factorize(36))
        => {2:2, 3:2}
    """
    a = []

    while n > 1:
        f = factors[n]
        a.append(f)
        n //= f

    return a

def find_minimum_factor(MAX):
    """
    MAX以下の自然数について「最小の素因数」を調べます。
    ある自然数nが素数ならば factors[n] == n です。
    """
    factors = [None] * (MAX+1)

    for i in range(2, len(factors)):
        if factors[i] is None:
            # log(i, "is prime.")
            factors[i] = i
            for j in range(i*2, len(factors), i):
                factors[j] = i

    return factors

def multi(l,r,n):
    """l以上r以下でnの倍数である自然数の個数"""
    return r//n - (l-1)//n

def product(iter):
    return reduce(lambda a,b:a*b, iter)

def main():
    l,r = INTS()

    if l==1:
        l+=1
    if r==1:
        print(0)
        return

    factors = find_minimum_factor(10**6+1)

    ans = 0
    for x in range(l,r):
        # xより大きくr以下の整数で、xとの公約数を持ち、かつxの倍数ではない整数の数を求める

        # xの素因数をp1, p2とすると、
        # 1～Rの中でxと公約数を持つ自然数の個数は以下(包除原理による)。
        # R/p1 + R/p2 - R/(p1*p2)
        # さらにxの倍数を省きたいので、上記から R/x を引いた個数になる。

        # xの素因数分解
        prime_factors = set(prime_factorize(x, factors))
        pn = len(prime_factors)

        # 素因数からi個取った組み合わせを全探索
        for i in range(1,pn+1):
            yn = 0
            for comb in combinations(prime_factors, i):
                prod = product(comb)
                yn += multi(x+1, r, prod)

            if i%2==0:
                # 偶数は引き算
                yn *= -1

            # (x,y)と(y,x)があるので2倍する
            ans += yn*2
        # xの倍数を省く
        ans -= multi(x+1,r,x)*2

    print(ans)

main()
