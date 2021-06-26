import sys
sys.setrecursionlimit(10**7)
def input(): return sys.stdin.readline().strip()
def INT():   return int(input())
def INTS():  return [ int(s) for s in input().split(" ")]
def log(*args, **kwargs): print("DEBUG:", *args, **kwargs, file=sys.stderr)

def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1]

def gaiseki(a,b):
    return a[0]*b[1] - a[1]*b[0]

def main():
    n = INT()
    S = []
    T = []
    for i in range(n):
        S.append(INTS())
    for i in range(n):
        T.append(INTS())

    if n == 1:
        print("Yes")
        return

    S0 = S[0]
    S1 = S[1]
    S0_1 = [S1[0]-S0[0], S1[1]-S0[1]]
    dis_0_1_squared = S0_1[0] ** 2 + S0_1[1] ** 2
    for i in range(n):
        Ti = T[i]
        for j in range(n):
            # S0_1と距離が等しいベクトルを見つける
            Tj = T[j]
            Ti_j = [Tj[0]-Ti[0], Tj[1]-Ti[1]]
            dis_i_j_squared = Ti_j[0]**2 + Ti_j[1]**2

            if dis_0_1_squared == dis_i_j_squared:
                found = True
                for k in range(n):
                    Sk = S[k]
                    # S0_1からみたS[k]と同じ位置にある点をTから探す
                    S0_k = [Sk[0]-S0[0], Sk[1]-S0[1]]
                    dot_01_0k = dot(S0_1, S0_k)
                    dis_0_k_squared = S0_k[0] ** 2 + S0_k[1] ** 2

                    ok = False

                    for l in range(n):
                        Tl = T[l]
                        Ti_l = [Tl[0]-Ti[0], Tl[1]-Ti[1]]
                        dot_ij_il = dot(Ti_j, Ti_l)
                        dis_i_l_squared = Ti_l[0]**2 + Ti_l[1]**2

                        g1 = gaiseki(S0_1, S0_k)
                        g2 = gaiseki(Ti_j, Ti_l)

                        # 距離, 内積, 外積の正負 が全部等しければ相対的に同じ位置にあるとみなせる
                        if dot_01_0k == dot_ij_il and dis_0_k_squared == dis_i_l_squared and sign(g1)==sign(g2):
                            ok = True
                            break
                    if not ok:
                        found = False
                        break
                if found:
                    print("Yes")
                    return

    print("No")

main()
