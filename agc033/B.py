import sys
sys.setrecursionlimit(200100)

h,w,n = map(int, input().split(" "))
sr,sc = map(int, input().split(" "))

s = input()
t = input()

stst = ""
for i in range(n):
    stst += s[i]
    stst += t[i]

def dfsx(pos, x):

    sl = s[pos:].count("L")
    sr = s[pos:].count("R")
    tl = t[pos:].count("L")
    tr = t[pos:].count("R")

    if x <= 0 or x > w or (sl - tr) >= x or x+(sr - tl) > w:
        # 落ちたらFalse
        return False
    
    if pos == 2*n:
        # 最後まで落ちていなければTrue
        return True
    
    g = stst[pos]
    a = dfsx(pos+1, x)
    b = dfsx(pos+1, x + int(g=="R") - int(g=="L")) if g in "RL" else a

    if pos % 2 == 0:
        # 落とす未来があればFalse
        return a and b
    else:
        # 落とさない未来があればTrue
        return a or b

def dfsy(pos, y):
    
    su = s[pos:].count("U")
    sd = s[pos:].count("D")
    tu = t[pos:].count("U")
    td = t[pos:].count("D")

    if y <= 0 or y > h or (su - td) >= y or y+(sd - tu) > h :
        # 落ちたらFalse
        return False
    
    if pos == 2*n:
        # 最後まで落ちていなければTrue
        return True
    
    g = stst[pos]
    a = dfsy(pos+1, y)
    b = dfsy(pos+1, y + int(g=="D") - int(g=="U")) if g in "UD" else a

    if pos % 2 == 0:
        # 落とす未来があればFalse
        return a and b
    else:
        # 落とさない未来があればTrue
        return a or b



print("YES" if dfsx(0, sc) and dfsy(0, sr) else "NO")
