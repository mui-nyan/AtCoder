# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

n,*A = get_all_int()

if min(A) == 0:
    print(0)
    exit()

ans = 1
for a in A:
    ans *= a

    if ans > 10**18:
        print(-1)
        exit()

print(ans)
