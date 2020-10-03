import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

n = int(input())
S = [ input() for _ in range(n)]

left = 0
right = 0

LMR = [0] * n
MIN_LMR = [0] * n

for i,s in enumerate(S):
    l = 0
    r = 0
    lok = True
    for j,c in enumerate(s):
        if c == "(":
            l += 1
        else:
            r += 1
            if r > l:
                lok = False
        MIN_LMR[i] = min(MIN_LMR[i], l-r)
    LMR[i] = l - r

    left += l
    right += r

if left != right:
    print("No")
    exit()


positives = [ (MIN_LMR[i], LMR[i]) for i,x in enumerate(LMR) if x > 0 ]
zeros     = [ (MIN_LMR[i], LMR[i]) for i,x in enumerate(LMR) if x == 0 ]
negatives = [ (MIN_LMR[i], LMR[i]) for i,x in enumerate(LMR) if x < 0]
for i in range(len(negatives)):
    # 負の要素だけ、裏返して末尾から見た値に変換する
    min_lmr, lmr = negatives[i]
    min_lmr = min_lmr - lmr
    lmr = -1 * lmr
    negatives[i] = (min_lmr, lmr)

positives.sort(reverse=True)
negatives.sort(reverse=True)

h = 0
for min_lmr, lmr in positives + zeros:
    if h+min_lmr < 0:
        print("No")
        exit()
    h += lmr

h = 0
for min_lmr, lmr in negatives:
    if h+min_lmr < 0:
        print("No")
        exit()
    h += lmr

print("Yes")
