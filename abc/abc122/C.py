

tmp = input().split(" ")
n = tmp[0]
q = int(tmp[1])

s = input()

ac_indexes=[]
start=0
while True:
    ind = s.find("AC", start)
    if ind != -1:
        start=ind+2
        ac_indexes.append(ind)
    else:
        break

memo = {}

for i in range(q):

    if len(ac_indexes) == 0:
        print ("0")
        continue

    tmp = input().split(" ")
    a = int(tmp[0]) - 1
    b = int(tmp[1]) - 2

    memo_ = memo.get(str(a) + "," + str(b))
    if memo_ != None:
        print (str(memo))


    left = 0
    right = len(ac_indexes)-1
    left_kari=-1
    left_kakutei = -1
    while left <= right:
        center = (left+right)//2
        if ac_indexes[center] > a:
            right = center-1
            left_kari = center
        elif ac_indexes[center] < a:
            left = center+1
        else:
            left_kakutei = center
            break
    if left_kakutei == -1:
        left_kakutei = left_kari
    
    left = 0
    right = len(ac_indexes)-1
    right_kari = -1
    right_kakutei = -1
    while left <= right:
        center = (left+right)//2
        #print (left, center, right)
        if ac_indexes[center] > b:
            right = center-1
        elif ac_indexes[center] < b:
            left = center+1
            right_kari = center
        else:
            right_kakutei = center
            break
    if (right_kakutei == -1):
        right_kakutei = right_kari

    if (left_kakutei > right_kakutei or left_kakutei==-1 or right_kakutei==-1):
        print ("0")
        continue

    print(str(right_kakutei - left_kakutei + 1))
    memo.update({str(a) + "," + str(b): (right_kakutei - left_kakutei + 1)})
