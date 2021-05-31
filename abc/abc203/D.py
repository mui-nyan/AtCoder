import sys
sys.setrecursionlimit(10**7)

def input(): return sys.stdin.readline().strip()
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args): print("DEBUG:", *args, file=sys.stderr)

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

        # log(center, zero_one_grid)

        ruiseki = [ [0] * (n+1) for _ in range(n+1)]
        for y in range(n):
            for x in range(n):
                ruiseki[y+1][x+1] = ruiseki[y][x+1] + ruiseki[y+1][x] - ruiseki[y][x] + zero_one_grid[y][x]
        
        # log(ruiseki)

        def get(t,l,b,r):
            return ruiseki[b][r] - ruiseki[t][r] - ruiseki[b][l] + ruiseki[t][l]

        ok = False
        for kt in range(n-k+1):
            for kl in range(n-k+1):
                # under = このk*k区間で、高さがcenter以下のマスの個数
                under = get(kt, kl, kt+k, kl+k)
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
