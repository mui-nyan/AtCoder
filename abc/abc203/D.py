import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args): print("DEBUG:", *args, file=sys.stderr)

class CumulativeSumOnGrid():
    """二次元累積和"""
    def __init__(self, grid):
        h = len(grid)
        w = len(grid[0])
        self.ruiseki = [ [0] * (w+1) for _ in range(h+1)]
        for y in range(h):
            for x in range(w):
                self.ruiseki[y+1][x+1] = grid[y][x] + self.ruiseki[y][x+1] + self.ruiseki[y+1][x] - self.ruiseki[y][x]

    def get(self,t,l,b,r):
        """
        指定した長方形区間の合計を取得します。
        区間は、元のgridに対する半開区間になります。
        [tl:br)
        """
        return self.ruiseki[b][r] - self.ruiseki[t][r] - self.ruiseki[b][l] + self.ruiseki[t][l]

def main():
    n, k = INTS()
    grid = []
    for i in range(n):
        grid.append(INTS())
    
    left = -1
    right = 10**9 + 1

    while left+1 < right:
        center = (left+right)//2

        # ok = 中央値がcenter以下になるk*kの区画が存在するか？
        # として、okの下限を求める
        
        # 中央値がX以下 ⇔ X以下の要素個数が半数以上ある
        # なので、値をX以下かどうかで0 or 1に変換してから二次元累積和で数える

        zero_one_grid = [
            [ 1 if x<=center else 0 for x in grid[i] ] for i in range(n)
        ]

        ruiseki = CumulativeSumOnGrid(zero_one_grid)

        ok = False
        for kt in range(n-k+1):
            for kl in range(n-k+1):
                # under = このk*k区間で、高さがcenter以下のマスの個数
                under = ruiseki.get(kt, kl, kt+k, kl+k)
                # log(y)
                if under >= (k**2+1)//2:
                    ok = True
                    break
            else:
                continue
            break

        # log("c:", center, "OK" if ok else "NG")

        if ok:
            right = center
        else:
            left = center
        
    print(right)

main()
