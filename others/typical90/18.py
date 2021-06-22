from math import sin, cos, atan2, pi, sqrt
import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    t = INT()
    l, x, y = INTS()
    r = l/2
    q = INT()
    for i in range(q):
        e = INT()
        # 観覧車の角度。時計回りに回るので-e/t。0分のとき-90°になるように90度引いておく
        theta = 2 * pi * (-e/t) - (pi/2)

        # 観覧車のy,z座標
        ky = cos(theta) * r
        kz = sin(theta) * r + r

        # 観覧車の影と石像のx,y平面上の距離
        d = sqrt(x**2 + (y-ky)**2)

        print(atan2(kz, d) * 180 / pi)

main()
