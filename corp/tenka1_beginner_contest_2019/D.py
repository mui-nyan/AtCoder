import math

n = int(input())

# 半分超過による枝刈りを早く起こすために降順に並べる
arr = sorted([ int(input()) for _ in range(n) ], reverse = True )


sum = 0
for x in arr:
    sum += x
half=sum/2

def over_red(pos, r):

    if pos == n:
        if r >= half:
            return 1
        else:
            return 0

    if memo[pos][r] != -1:
        return memo[pos][r]
    
    val = over_red(pos+1, r) * 2 + over_red(pos+1, r + arr[pos])
    memo[pos][r] = val

    return val

def just_half(pos, r):
    if pos == n:
        if r == half:
            return 1
        else:
            return 0
    
    if r > half:
        return 0

    if memo[pos][r] != -1:
        return memo[pos][r]
    
    val = just_half(pos+1, r) + just_half(pos+1, r + arr[pos])
    memo[pos][r] = val
    return val

# 全体のパターン数
all_patterns = 3 ** n

# 赤が半分を超過するパターン数 * 3
memo=[ [ -1 for _ in range(sum)] for _ in range(n)]
over_red_patterns = over_red(0,0)*3

# 赤と青がちょうど半分ずつになるパターン数 * 3
memo=[ [ -1 for _ in range(sum)] for _ in range(n)]
just_half_patterns = just_half(0,0) * 3

# 全体 - (Rが超過)*3 + (RとBがちょうど半分)*3
print( (all_patterns - over_red_patterns + just_half_patterns)  % 998244353 )
