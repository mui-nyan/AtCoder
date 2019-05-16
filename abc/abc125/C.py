from functools import reduce

def gcd(m, n):
    # 入力を m, n (m ≧ n) とする。
    tmp = max(m,n)
    n = min(m,n)
    m = tmp
    # n = 0 なら、 m を出力してアルゴリズムを終了する。
    if n == 0:
        return m
    # m を n で割った余りを新たに n とし、更に 元のnを新たにm とし 2. に戻る。
    return gcd(n, m % n)

n = int(input())
nums = [ int(s) for s in input().split(" ")]

if n == 2:
    print(max(nums))
    exit()

left_n = [0 for _ in range(n)]
right_n = [0 for _ in range(n)]

left_n[0] = nums[0]
right_n[n-1] = nums[n-1]

for i in range(n-1):
    left_n[i+1] = gcd(left_n[i], nums[i+1])
    right_n[n-2-i] = gcd(right_n[n-1-i], nums[n-2-i])


maxgcd = 0
for i in range(n):
    if i == 0:
        maxgcd = max(maxgcd, right_n[1])
    if i == n-1:
        maxgcd = max(maxgcd, left_n[n-2])
    else:
        maxgcd = max(maxgcd, gcd(right_n[i+1], left_n[i-1]))

print(maxgcd)
