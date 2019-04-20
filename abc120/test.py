
def x(n):
    if n == 0:
        return 0
    else:
        return x(n-1)

print (x(998))