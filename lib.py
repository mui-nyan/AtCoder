
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

def lcm(m, n):
    return m*n//gcd(m,n)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

def fac(N):
    MOD = 10**9 + 7
    known = { 0: 1, 1000000000: 698611116, 320000000: 30977140, 820000000: 629786193, 740000000: 375297772, 470000000: 909210595, 200000000: 933245637, 940000000: 83868974, 400000000: 429277690, 130000000: 623534362, 870000000: 256473217, 600000000: 724464507, 330000000: 522049725, 60000000: 27368307, 800000000: 203191898, 530000000: 256141983, 260000000: 135498044, 730000000: 663307737, 460000000: 275105629, 190000000: 109838563, 930000000: 778983779, 660000000: 769795511, 390000000: 917084264, 120000000: 661224977, 860000000: 116667533, 10000000: 682498929, 590000000: 131772368, 50000000: 67347853, 790000000: 748510389, 520000000: 608823837, 250000000: 112390913, 990000000: 847549272, 720000000: 852304035, 450000000: 462639908, 180000000: 547665832, 920000000: 193781724, 650000000: 92255682, 380000000: 940567523, 110000000: 281863274, 850000000: 823845496, 580000000: 848924691, 310000000: 128487469, 40000000: 723816384, 780000000: 624500515, 510000000: 97830135, 240000000: 136026497, 980000000: 377329025, 710000000: 435887178, 440000000: 780072518, 170000000: 66404266, 20000000: 491101308, 670000000: 373745190, 910000000: 172114298, 640000000: 903466878, 370000000: 148528617, 100000000: 927880474, 840000000: 814362881, 570000000: 811575797, 300000000: 668123525, 30000000: 76479948, 770000000: 671734977, 500000000: 733333339, 230000000: 268838846, 970000000: 492741665, 700000000: 957939114, 430000000: 568392357, 160000000: 195888993, 900000000: 586445753, 630000000: 456152084, 360000000: 189239124, 90000000: 888050723, 830000000: 672850561, 560000000: 637939935, 290000000: 500780548, 760000000: 624148346, 490000000: 703397904, 220000000: 368925948, 270000000: 217544623, 960000000: 965785236, 690000000: 825871994, 420000000: 358655417, 150000000: 261384175, 890000000: 245795606, 620000000: 326159309, 350000000: 386027524, 80000000: 199888908, 550000000: 696628828, 280000000: 419363534, 750000000: 217598709, 480000000: 99199382, 210000000: 724691727, 950000000: 315103615, 680000000: 606241871, 410000000: 996164327, 140000000: 970055531, 880000000: 627655552, 610000000: 272814771, 340000000: 309058615, 70000000: 625544428, 810000000: 423951674, 540000000: 141827977}

    ans = known[ N - N % int( 1e7 ) ]
    for i in range( N - N % int( 1e7 ) + 1, N + 1, 1 ):
        ans = ans * i % MOD
    return ans

def init_kaijo(MAX, MOD):
    kaijo = [0] * MAX
    kaijo[0] = 1
    for i in range(1, len(kaijo)):
        kaijo[i] = kaijo[i-1] * i % MOD
    return kaijo
kaijo = init_kaijo(500000, 10**9+7)

def inv(x, MOD):
    return pow(x, MOD-2, MOD)

def nPk(n, k, MOD):
    return kaijo[n] * inv(kaijo[n-k], MOD) % MOD

def nCk(n, k, MOD):
    return nPk(n,k, MOD) * inv(kaijo[k], MOD)

def nHk(n, k, MOD):
    return nCk(n+k-1, k, MOD)

from itertools import combinations
def subsets(items):
    _subsets_=[]
    for i in range(len(items) + 1):
        for c in combinations(items, i):
            _subsets_.append(c)
    return _subsets_

def init_primes(MAX):
    primes = [None] * MAX

    for i in range(2, len(primes)):
        if primes[i] is None:
            # log(i, "is prime.")
            primes[i] = True
            for j in range(i*2, len(primes), i):
                primes[j] = False

    return primes

# 昇順にソート済みのarrにnが存在すれば、最も左のindexと値を返します。
# 存在しない場合は、Noneを返します。
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
    c = max(0, (l+r)//2)
    if arr[c] == n:
        return (c, arr[c])
    else:
        return None

# 昇順にソート済みのarrから、n以上の最小の要素を探索して返します。
# 存在しない場合は、Noneを返します。
def bin_gte(arr, n):
    l = 0
    r = len(arr) - 1
    c = (l+r)//2
    while l < r:
        c = (l+r)//2
        if arr[c] >= n:
            r = c
        else :
            l = c+1
    c = max(0, (l+r)//2)
    if arr[c] >= n:
        return (c, arr[c])
    else:
        return None

# 昇順にソート済みのarrから、n以下の最大の要素を探索して返します。
# 存在しない場合は、Noneを返します。
def bin_lte(arr, n, l):
    r = len(arr) - 1
    c = (l+r)//2
    while l < r:
        c = (l+r+1)//2
        if arr[c] <= n:
            l = c
        else :
            r = c-1
    c = max(0, (l+r)//2)
    if arr[c] <= n:
        return (c, arr[c])
    else:
        return None

def neighbors8(x, y):
  dxy = (1, 1, 0, 1, -1, 0, -1, -1, 1 )
  for i in range(8):
    yield(x + dxy[i], y + dxy[i+1])

def neighbors4(x, y):
  dxy = (0, 1, 0, -1, 0 )
  for i in range(4):
    yield(x + dxy[i], y + dxy[i+1])


class segtree:
    def __init__(self, n,operator,identity):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.num_end_leaves = 2**(len(nb)-1)
        else:
            self.num_end_leaves = 2**(len(nb))

        self.array = [identity for i in range(self.num_end_leaves * 2)]
        self.identity = identity
        self.operator =operator

    def update(self,x,val):
        actual_x = x+self.num_end_leaves
        self.array[actual_x] = val
        while actual_x > 0 :
            actual_x = actual_x//2
            self.array[actual_x] = self.operator(self.array[actual_x*2],self.array[actual_x*2+1])

    def get(self,q_left,q_right,arr_ind=1,leaf_left=0,depth=0):
        """
        [q_left, q_right] (閉区間) の値を集計して返します。
        """

        width_of_floor = self.num_end_leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if leaf_left > q_right or leaf_right < q_left:
            return  self.identity

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[arr_ind]

        else:
            val_l = self.get(q_left,q_right,2*arr_ind,leaf_left,depth+1)
            val_r = self.get(q_left,q_right,2*arr_ind+1,leaf_left+width_of_floor//2,depth+1)
            return self.operator(val_l,val_r)

##
# Union-Find
nodes = 99999999999
node_groups = [ i for i in range(nodes)]
group_sizes = [ 1 for _ in range(nodes)]
group_ranks = [ 0 for _ in range(nodes)]

m = 99999
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

