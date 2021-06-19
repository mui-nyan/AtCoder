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

def main():
    n = INT()
    A = INTS()

    if A == A[::-1]:
        print(0)
        return

    uf = union_find(200009)
    ans = 0
    for i in range((n)//2):
        j = n-i-1

        if A[i] != A[j] and not uf.same(A[i], A[j]):
            uf.unite(A[i],A[j])
            ans += 1
    
    print(ans)

main()
