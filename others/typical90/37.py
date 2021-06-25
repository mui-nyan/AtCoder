import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def get(self, i):
        """ [i] の値を返します。 query(i, i+1) と同じ結果を返しますが、より高速に結果を返します。"""
        return self.dat[self.size + i]

    def query(self, l, r):
        """ [l, r) (半開区間) の範囲を計算して返します。"""
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

def main():
    w, n = INTS()

    menu = []
    for i in range(n):
        l,r,v = INTS()
        menu.append((l,r,v))

    # dp[i%2][j] = i個までの料理を考慮して、香辛料をj消費した場合の価値の最大値
    dp = [ SegmentTree(w+1, f=max, default=-1) for _ in range(2) ]

    for i in range(2):
        dp[i].update(0, 0)

    for i in range(n):
        ii = i+1
        now = dp[ii%2]
        prev = dp[i%2]
        l,r,v = menu[i]
        for j in range(1, w+1):
            # 直前の状態はそのまま引き継ぐ
            prev_val = prev.get(j)

            # x = この料理を使った結果香辛料の消費量がちょうどjにできるような、直前の選び方の最大の価値
            x = -1
            if j-l+1 > 0:
                x = prev.query(max(0,j-r), max(0,j-l+1))
            now.update(j, max(prev_val, x+v) if x != -1 else prev_val)

    print(dp[n%2].query(w,w+1))

main()
