import sys
import queue

sys.setrecursionlimit(200000)



h,w = map(int, input().split(" "))

black_table = [ [ 0 if c == "#" else 99999999 for c in input() ] for _ in range(h) ]

#print(black_table)


qsize= 0
def push(y, x, n):
    global qsize
    qsize += 1
    blacks.put([y,x,n])

def pop():
    global qsize
    qsize -= 1
    return blacks.get()

def can():
    return qsize > 0

def erosion(y, x, n):
    if n < black_table[y][x] or n == 0:
        black_table[y][x] = n

        if y < h-1:
            push(y+1, x, n+1)
        if y > 0:
            push(y-1, x, n+1)
        if x < w-1:
            push(y, x+1, n+1)
        if x > 0:
            push(y, x-1, n+1)


blacks = queue.Queue()

for y in range(h):
    for x in range(w):
        if black_table[y][x] == 0:
            push(y,x,0)

while can():
    b = pop()
    erosion(b[0], b[1], b[2])

max_dis = 0

for array in black_table:
    max_dis = max(max_dis, max(array))

print(max_dis)