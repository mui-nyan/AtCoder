tmp=input().split(" ")
a = int(tmp[0])
b = int(tmp[1])

if a == b:
    print (a*2)
else:
    print (max(a,b)*2-1)
