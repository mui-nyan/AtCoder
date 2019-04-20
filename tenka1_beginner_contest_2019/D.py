import math

n = int(input())
arr = sorted([ int(input()) for _ in range(n) ], reverse=True)

sum = 0
for x in arr:
    sum += x
half=sum/2

memo=[[[ -1 for _ in range(math.ceil(half))] for _ in range(math.ceil(half))] for _ in range(math.ceil(half))]

def f(r,g,b,cur):
    if r >= half or g >= half or b >= half:
        return 0
    if cur == n:
        return 1
    tmp = sorted([r,g,b])
    m1 = tmp[2]
    m2 = tmp[1]
    m3 = tmp[0]
    if memo[m1][m2][m3] != -1:
       return memo[m1][m2][m3]
    memo[m1][m2][m3] = (f(r + arr[cur], g, b, cur+1) + f(r, g+arr[cur], b, cur+1) + f(r, g, b+arr[cur], cur+1)) % 998244353
    return memo[m1][m2][m3]
    # return(f(r + arr[cur], g, b, cur+1) + f(r, g+arr[cur], b, cur+1) + f(r, g, b+arr[cur], cur+1)) % 998244353

print(f(0,0,0,0))
