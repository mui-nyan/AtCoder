# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

MOD = 10**9+7

n,*A = get_all_int()

pow2 = [1] * 61
for i in range(1,61):
    pow2[i] = pow2[i-1] * 2

# ビットごとの出現回数 2**i
bits = [0] * 60

for a in A:
    for i in range(60):
        if pow2[i] & a != 0:
            bits[i] += 1

# その位のビットの1の個数*0の個数 が、そのビットがansに足される回数
ans = sum(( pow(2, i, MOD) * bits[i] * (n-bits[i]) for i in range(60))) % MOD

print(ans)
