n = int(input())
s = input()

max_count=0
for i in range(1,n):
    left = s[:i]
    right = s[i:]
    count = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in left and c in right:
            count += 1
    max_count = max(max_count, count)

print(max_count)