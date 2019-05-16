tmp=input().split(" ")
n = int(tmp[0])
initialPoint = int(tmp[1])

points= [ abs(int(s)-initialPoint) for s in input().split(" ") ]

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

if n == 1:
    print(points[0])
    exit()

now=gcd(points[0], points[1])
for i in range(2, len(points)):
    now = gcd(now, points[i])

print(now)