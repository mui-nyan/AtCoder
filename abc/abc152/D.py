import math

n = int(input())

keta = int(math.log10(n)) + 1

memo = [ [None] * 10 for _ in range(10)]

ans = 0
for a in range(1, n+1):
    x = int(str(a)[0])
    y = a % 10

    if x == 0 or y == 0:
        continue

    if memo[x][y] is not None:
        ans += memo[x][y]
        # print(a, ans)
        continue
    
    patterns = 0
    for b in range(x, n+1, 10):
        x2 = int(str(b)[0])
        y2 = b % 10
        if x == y2 and y == x2:
            patterns += 1
    memo[x][y] = patterns
    ans += patterns

print(ans)