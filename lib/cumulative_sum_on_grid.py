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
