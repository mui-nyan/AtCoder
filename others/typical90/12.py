import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

class union_find():
    def __init__(self, n):
        self.nodes = n
        self.node_groups = [ i for i in range(n)]
        self.group_sizes = [ 1 for _ in range(n)]
        self.group_ranks = [ 0 for _ in range(n)]

    def root(self, i):
        if self.node_groups[i] == i:
            return i
        else:
            self.node_groups[i] = self.root(self.node_groups[i])
            return self.node_groups[i]

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, i):
        return self.group_sizes[self.root(i)]

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)

        if a == b:
            return

        if self.group_ranks[a] < self.group_ranks[b]:
            self.group_sizes[b] += self.size(a)
            self.node_groups[a] = b
        else:
            self.group_sizes[a] += self.size(b)
            self.node_groups[b] = a
            if self.group_ranks[a] == self.group_ranks[b]:
                self.group_ranks[a] += 1

def neighbors4(x, y):
    dxy = (0, 1, 0, -1, 0 )
    for i in range(4):
        yield(x + dxy[i], y + dxy[i+1])

def main():
    h,w = INTS()
    grid = [ [False] * (w) for _ in range(h) ]

    # uf木の上でsameならば相互に通行可能
    # 1次元配列なのでマス(y,x)のインデックスは [y*w + x]
    uf = union_find(h*w)
    
    for _ in range(INT()):
        cmd, *Q = INTS()
        if cmd == 1:
            y,x = Q
            y-=1
            x-=1

            # 指定されたマスを赤とマークする
            grid[y][x] = True

            # 隣に赤マスがあれば相互に通行可能なグループとして記録する
            for nx, ny in neighbors4(x, y):
                if nx>=0 and nx<w and ny>=0 and ny<h:
                    if grid[ny][nx]:
                        uf.unite(y*w + x, ny*w + nx)
        else:
            ay, ax, by, bx = Q
            ay-=1
            ax-=1
            by-=1
            bx-=1
            # 始点と終点が赤 かつ 通行可能(uf木の上で同じグループ)
            if grid[ay][ax] and grid[by][bx] and uf.same(ay*w+ax, by*w+bx):
                print("Yes")
            else:
                print("No")

main()
