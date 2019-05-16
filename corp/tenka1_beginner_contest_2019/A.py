tmp = input().split(" ")
a = int(tmp[0])
b = int(tmp[1])
c = int(tmp[2])

if a < c and c < b or b < c and c < a:
    print("Yes")
else:
    print("No")