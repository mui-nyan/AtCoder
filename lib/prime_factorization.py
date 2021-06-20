def prime_factorize(n, factors=None):
    """
    nを素因数分解します。
    factors(自然数の最小素因数リスト)が与えられる場合、O(log(n))の計算量で計算できます。
    その他の場合にはO(√n)の計算量で計算できます。

    Sample:
        prime_factorize(36)
        => [2, 2, 3, 3]

        collections.Counter(prime_factorize(36))
        => {2:2, 3:2}
    """
    a = []
    if factors is not None:
        while n > 1:
            f = factors[n]
            a.append(f)
            n //= f
    else:
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)

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
                if factors[j] is None:
                    factors[j] = i

    return factors
