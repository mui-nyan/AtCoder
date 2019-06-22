
def gcd(m, n):
    # 入力を m, n (m ≧ n) とする。
    tmp = max(m,n)
    n = min(m,n)
    m = tmp
    # n = 0 なら、 m を出力してアルゴリズムを終了する。
    if n == 0:
        return m
    # m を n で割った余りを新たに n とし、更に 元のnを新たにm とし 2. に戻る。
    return gcd(n, m % n)

# 昇順にソート済みのarrにnが存在すれば、最も左のindexを返します。
# 存在しない場合は、-1を返します。
def bin_eq(arr, n):
    l = 0
    r = len(arr) - 1
    c = (l+r)//2
    while l < r:
        c = (l+r)//2
        if arr[c] > n:
            r = c-1
        elif arr[c] < n:
            l = c+1
        else:
            r = c
    c = (l+r)//2
    if arr[c] == n:
        return c
    else:
        return -1

##
# Union-Find
nodes = 99999999999
node_groups = [ i for i in range(nodes)]
group_sizes = [ 1 for _ in range(nodes)]
group_ranks = [ 0 for _ in range(nodes)]

edges = []
for i in range(m):
    tmp=input().split(" ")
    edges.append([int(tmp[0])-1, int(tmp[1])-1])


def root(i):
    if node_groups[i] == i:
        return i
    else:
        node_groups[i] = root(node_groups[i])
        return node_groups[i]

def same(a, b):
    return root(a) == root(b)

def size(i):
    return group_sizes[root(i)]

def unite(a, b):
    a = root(a)
    b = root(b)

    if a == b:
        return

    if group_ranks[a] < group_ranks[b]:
        group_sizes[b] += size(a)
        node_groups[a] = b
    else:
        group_sizes[a] += size(b)
        node_groups[b] = a
        if group_ranks[a] == group_ranks[b]:
            group_ranks[a] += 1

