import math

tmp = [ int(a) for a in input().split(" ")]
x = tmp[0]
y = tmp[1]
z = tmp[2]
k = tmp[3]

a_arr = sorted([ int(a) for a in input().split(" ")], reverse=True)
b_arr = sorted([ int(a) for a in input().split(" ")], reverse=True)
c_arr = sorted([ int(a) for a in input().split(" ")], reverse=True)

ai=0
bi=0
ci=0
prev=0
for i in range(k-1):

    next_a = a_arr[ai + 1] if ai+1 < x else -1
    next_b = b_arr[bi + 1] if bi+1 < y else -1
    next_c = c_arr[ci + 1] if ci+1 < z else -1

    if next_a > next_b and next_a > next_c:
        ai += 1
        bi = 0
        ci = 0
    elif next_b > next_c:
        bi += 1
    else:
        ci += 1
    print(a_arr[ai] + b_arr[bi] + c_arr[ci])

check_sheet = [False] * (x*y*z)
def mark(a, b, c):
    check_sheet[a*(y*z) + b*z + c] = True

def is_checked(a, b, c):
    return check_sheet[a*(y*z) + b*z + c]
