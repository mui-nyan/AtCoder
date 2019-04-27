n=int(input())
values = [ int(s) for s in input().split(" ") ]
costs = [ int(s) for s in input().split(" ") ]

ans=0
for i in range(n):
    if values[i] > costs[i]:
        ans += values[i] - costs[i]

print(ans)
