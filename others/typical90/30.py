import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def find_factors(MAX):
    """
    MAX以下の自然数について「素因数の種類数」を調べます。
    ある自然数nが素数ならば factors[n] == 1 です。
    """
    factors = [0] * (MAX+1)

    for i in range(2, len(factors)):
        if factors[i] == 0:
            factors[i] = 1
            for j in range(i*2, len(factors), i):
                factors[j] += 1

    return factors

def main():
    n, k = INTS()
    factors = find_factors(n)
    ans = 0
    for a in factors:
        if a >= k:
            ans += 1
    print(ans)

main()
