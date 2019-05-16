def s(generator, splitter, mapper):
    return [ mapper(s) for s in generator().split(splitter) ]

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行区切りの入力をn行読み込んで数値リストにして返します。
def get_nums_n(n):
    return [ int(input()) for _ in range(n)]

MOD = 10 ** 9 + 7

n = int(input())
nums = get_nums_l()

ruiseki_xor = [ 0 for _ in range(n+1) ]

for i,n in enumerate(nums):
    ruiseki_xor[i+1] = ruiseki_xor[i] ^ n

def span_xor(l, r):
    return ruiseki_xor[r+1] ^ ruiseki_xor[l]

xor_patterns = set(ruiseki_xor)

def f(xor, now_xor, pos):
    new_xor = now_xor ^ nums[pos]

    if pos == n-1:
        return 0 if new_xor == xor else 1

    if xor != new_xor:
        # ここで切るパターンは全部だめ
        ng = 2 ** (n-pos-2)

        # ここで切らないパターンと足して返す
        return ng + f(xor, new_xor, pos+1)
    else:
        # 切るパターンと切らないパターンを足して返す
        return f(xor, new_xor, pos+1) + f(xor, 0, pos+1)

ans = 2 ** (n-1)
for i,x in enumerate(ruiseki_xor):
    if i in [0,n]:
        continue
    a = f(x, 0, i)
    print(x, a)
    ans -= a

print(ans)