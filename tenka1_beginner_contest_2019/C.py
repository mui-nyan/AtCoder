n = int(input())
s = input()

left_blacks = [0] * (n + 1)
right_whits = [0] * (n + 1)
for i in range(n):
    left_blacks[i+1] = left_blacks[i] + 1 if s[i] == "#" else left_blacks[i]

for i in range(n, 0, -1):
    right_whits[i-1] = right_whits[i] + 1 if s[i-1] == "." else right_whits[i]

ans = 9999999999999999999
for i in range(n+1):
    ans = min(ans, left_blacks[i] + right_whits[i])

print(ans)