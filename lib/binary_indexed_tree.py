class BinaryIndexedTree:
    """BITは1-indexed"""
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        """tree[i]まで(1-indexed, iを含む)の合計を取得します。"""
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        """tree[i](1-indexed)にxを加算します。"""
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
