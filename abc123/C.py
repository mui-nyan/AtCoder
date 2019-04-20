import math

n = int(input())

arr=[int(input()),int(input()),int(input()),int(input()),int(input())]

min=arr[0]

for capa in arr:
    if capa < min:
        min = capa

print(math.ceil(n/min) + 4)