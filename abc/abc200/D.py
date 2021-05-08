import math
from functools import reduce
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

# 改行またはスペース区切りの入力をすべて読み込んでイテレータを返します。
def get_all_int():
    return map(int, open(0).read().split())

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)


def findfront(x, A):
    for i,a in enumerate(A):
        if a == x:
            return i
def findback(x, A):
    for i,a in reversed(list(enumerate(A))):
        if a == x:
            return i

def main():
    INF = 999999999999999999999999
    MOD = 10**9+7

    n,*A = get_all_int()

    A = list(map(lambda a: a%200, A))
    mod200 = defaultdict(int)
    for a in A:
        mod200[a] += 1
    # log(mod200.keys())
    # log(A)
    # kaisa = []
    # for i in range(n-1):
    #     kaisa.append(A[i+1] - A[i])
    # log(kaisa)

    B = []
    C = []

    # modが等しい組があればそれを選択して終了
    if max(mod200.values()) >= 2:
        for m,c in mod200.items():
            if c >= 2:
                dbl = list(filter(lambda t: t[1]==m, enumerate(A)))
                B = [dbl[0][0]]
                C = [dbl[1][0]]
    else:
        end = False
        nodes = []
        edge_from = defaultdict(set)
        edge_to = defaultdict(set)
        for a in A:
            if end:
                break
            edge_from[-1].add(a)
            edge_to[a].add(-1)
            for node in nodes:
                edge_from[node].add((node + a) % 200)
                edge_to[(node + a) % 200].add(node)
                if len(edge_to[(node + a) % 200]) > 1:
                    # ペア発見
                    m = (node + a) % 200
                    B = []
                    C = []

                    # log(m)
                    # log(edge_to[m])

                    x1, x2 = edge_to[m]
                    prev = m
                    while x1 != -1:
                        p = (prev - x1) % 200
                        # log("x1", x1, "p", p)
                        # log(findfront(p, A))
                        B.append(findfront(p, A))
                        prev=x1
                        for k in edge_to[x1]:
                            x1 = k

                    B.append(findfront(prev, A))

                    prev = m
                    while x2 != -1:
                        p = (prev - x2) % 200
                        # log("x2", x2, "p", p)
                        C.append(findback(p, A))
                        prev=x2
                        for k in edge_to[x2]:
                            x2 = k

                    C.append(findback(prev, A))

                    end = True
                    break

            nodes.append(a)

    if len(B) > 0:
        print("Yes")
        log(B)
        B = list(sorted(map(lambda i: i+1, B)))
        C = list(sorted(map(lambda i: i+1, C)))
        print(len(B), *B)
        print(len(C), *C)
    else:
        print("No")

main()
