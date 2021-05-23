def init_kaijo(MAX, MOD):
    kaijo = [0] * MAX
    kaijo[0] = 1
    for i in range(1, len(kaijo)):
        kaijo[i] = kaijo[i-1] * i % MOD
    return kaijo
kaijo = init_kaijo(500000, 10**9+7)

def inv(x, MOD):
    return pow(x, MOD-2, MOD)

def nPk(n, k, MOD):
    return kaijo[n] * inv(kaijo[n-k], MOD) % MOD

def nCk(n, k, MOD):
    return nPk(n,k, MOD) * inv(kaijo[k], MOD)

def nHk(n, k, MOD):
    return nCk(n+k-1, k, MOD)
