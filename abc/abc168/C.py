import math
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

INF = 999999999999999999999999
MOD = 10**9+7

a,b,h,m = get_all_int()
theta_h = math.radians(360 * (h/12+m/60/12))
theta_m = math.radians(360 * (m/60))

hx = math.cos(theta_h) * a
hy = math.sin(theta_h) * a
mx = math.cos(theta_m) * b
my = math.sin(theta_m) * b

dx = abs(hx - mx)
dy = abs(hy - my)

print(math.sqrt(dx**2 + dy**2))
