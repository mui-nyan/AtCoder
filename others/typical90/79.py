import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def main():
    h,w = INTS()

    A = []
    for y in range(h):
        A.append(INTS())
    B = []
    for y in range(h):
        B.append(INTS())
    
    ans = 0
    # 戦略:
    #   値を変化させる方法が1つしかないマスから順に操作回数を決定していく。
    #   初期状態では最も左上のマスが該当する。
    #   最も左上のマスの操作回数を決定したあとは、一つ右隣のマスが「値を変化させる方法が1つしかないマス」になる。
    #   (最も左上のマスを操作することでも値を変化させられるが、それをすると最初に値を合わせた部分が壊れてしまうので操作できない)
    #   これを繰り返して操作可能なマスを操作し終わったあと、AとBが一致しているかを調べる。

    # 右端、下端は選べないのでループの終端を-1する。
    for y in range(h-1):
        for x in range(w-1):
            diff = B[y][x] - A[y][x]
            ans += abs(diff)

            A[y][x] += diff
            A[y+1][x] += diff
            A[y][x+1] += diff
            A[y+1][x+1] += diff

    ok = True
    for y in range(h):
        for x in range(w):
            if A[y][x] != B[y][x]:
                ok =False
                break

    if ok:
        print("Yes")
        print(ans)
    else:
        print("No")

main()
