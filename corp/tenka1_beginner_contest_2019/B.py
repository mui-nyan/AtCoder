n = int(input())
s = input()
k = int(input())

x = s[k-1]

ans=""
for c in s:
    if c != x:
        ans += "*"
    else:
        ans += c

print(ans)