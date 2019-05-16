tmp=input().split(" ")
h = int(tmp[0])
w = int(tmp[1])

coin_map = [ [ int(s) for s in input().split(" ")] for _ in range(h) ]
# print(coin_map)

n=0
history=[]

def move(x1,y1,x2,y2):
    global n
    n += 1
    history.append([y1+1, x1+1, y2+1, x2+1])
    coin_map[y1][x1] -= 1
    coin_map[y2][x2] += 1

for y in range(h):
    for x in range(w):
        if coin_map[y][x] % 2 == 1:
            if x < w-1:
                move(x,y, x+1,y)
            elif y < h-1:
                move(x,y, x,y+1)

print(n)

for i in range(n):
    print(" ".join(map(lambda n:str(n), history[i])))