n = int(input())
s = input()

left = [0]*n
for i,c in enumerate(s):
    if i == n-1:
        continue
    left[i+1] = left[i] + ( 1 if c == "W" else 0 )

right = [0] * n
for i,c in reversed(list(enumerate(s))):
    if i == 0:
        continue
    right[i-1] = right[i] + ( 1 if c == "E" else 0 )

min_cost=99999999999999999999

for i in range(n):
    min_cost = min(min_cost, left[i] + right[i])

print(min_cost)