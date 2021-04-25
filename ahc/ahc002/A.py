from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)
from time import time

def input():
    return sys.stdin.readline().strip()

# スペース区切りの入力を読み込んで数値リストにして返します。
def get_nums_l():
    return [ int(s) for s in input().split(" ")]

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

class TLEError(Exception):
    def __init__(self):
        pass

z_max_score = 0
z_ans = None

back_his = defaultdict(lambda:defaultdict(lambda:defaultdict(int)))

def main():

    stime = time()

    INF = 999999999999999999999999
    MOD = 10**9+7

    sy, sx = get_nums_l()
    t = []
    for y in range(50):
        t.append(get_nums_l())
    p = []
    for y in range(50):
        p.append(get_nums_l())
    

    def back(ret):
        score, ans, back = max(ret)
        # 枝刈りカウントを1減らして返す
        return (score, ans, back-1)

    def solve(y, x, now_score, moved_tiles, move_history, last_move, depth):
        global z_max_score, z_ans

        if t[y][x] in moved_tiles:
            # 移動済みタイル
            # 同じマスで何度も行き止まっている場合は枝刈りする
            back_his[y][x][depth] += 1
            return now_score, move_history, back_his[y][x][depth]//6

        now_score += p[y][x]
        moved_tiles.add(t[y][x])
        move_history.append(last_move)
        depth+=1
        
        if now_score > z_max_score:
            z_max_score = now_score
            z_ans = list(move_history)

        if time()-stime > 1.85:
            raise TLEError()

        ret = []

        if y-1>0:
            ret.append(solve(y-1, x, now_score, moved_tiles, move_history, "U", depth))
            if(ret[-1][2] > 1):
                move_history.pop(-1)
                moved_tiles.remove(t[y][x])
                return back(ret)
        if y+1<50:
            ret.append(solve(y+1, x, now_score, moved_tiles, move_history, "D", depth))
            if(ret[-1][2] > 1):
                move_history.pop(-1)
                moved_tiles.remove(t[y][x])
                return back(ret)
        if x-1>0:
            ret.append(solve(y, x-1, now_score, moved_tiles, move_history, "L", depth))
            if(ret[-1][2] > 1):
                move_history.pop(-1)
                moved_tiles.remove(t[y][x])
                return back(ret)
        if x+1<50:
            ret.append(solve(y, x+1, now_score, moved_tiles, move_history, "R", depth))
            if(ret[-1][2] > 1):
                move_history.pop(-1)
                moved_tiles.remove(t[y][x])
                return back(ret)

        score, ans, _ = max(ret)
        ans = list(ans)

        move_history.pop(-1)
        moved_tiles.remove(t[y][x])

        return score, ans, 0

    try:
        max_score, ans, _ = solve(sy, sx, 0, set(), [], "", 0)
        # print(max_score)
        log(max_score)
        print("".join(ans))
    except TLEError:
        # print(z_max_score)
        log(z_max_score)
        print("".join(z_ans))

main()
