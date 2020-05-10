from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().strip()

def log(*args):
    print("DEBUG:", *args, file=sys.stderr)

INF = 999999999999999999999999
MOD = 10**9+7

n = int(input())
s1 = input()
s2 = input()

nums = [ {0,1,2,3,4,5,6,7,8,9} for _ in range(n) ]
appears = defaultdict(set)

for s in (s1,s2):
    for i,c in enumerate(s):
        appears[c].add(i)

log(appears)

cons = deque()
cons.append((0, {1,2,3,4,5,6,7,8,9}))

for s in (s1,s2):
    for i,c in enumerate(s):
        if s[i].isdecimal():
            cons.append((i, { int(s[i]) }))

while cons:
    i, num = cons.popleft()
    log(i, num)
    if nums[i] - num:
        newnum = nums[i] & num
        nums[i] = newnum

        for c in (s1[i], s2[i]):
            if not c.isdecimal():
                for j in appears[c]:
                    if i != j:
                        cons.append((j, newnum))

log(nums)

ans = 1
for i, num in enumerate(nums):
    if s1[i] in s1[:i] or s2[i] in s2[:i] or s1[i] in s2[:i] or s2[i] in s1[:i]:
        continue
    ans *= len(num)
print(ans)
