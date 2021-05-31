from random import randint

D = randint(100, 2000)
# M = randint(1,2)
M = 2
H = [ [0] * M for _ in range(30)]

for i in range(30):
    for p in range(M):
        H[i][p] = randint(1000+D, 9000-D)

X = [ [0] * (M+1) for _ in range(30)]
for i in range(30):
    X[i][0] = 0
    X[i][M] = 29
    if M == 2:
        X[i][1] = randint(1,28)

E = [ [0] * 29 for _ in range(30)]
for i in range(30):
    for j in range(29):
        E[i][j] = randint(-D, D)

h = [ [0]*29 for _ in range(30)]

for i in range(30):
    for p in range(M):
        for j in range(X[i][p], X[i][p+1]):
            h[i][j] = H[i][p] + E[i][j]

for hh in h:
    print(hh)
