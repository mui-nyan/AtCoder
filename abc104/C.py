def can(d,g,p,c, maxPick):
	# n問解いてg点獲得できるか？

	# パーフェクトを狙う問題の組み合わせを生成
	for i in range(0, 2**(d-1)):

		# このパーフェクトのとり方で条件が達成できるか？
		point = 0
		picked = 0
		for j in range(0, d-1):
			if i & (2**j) != 0:
				point += (j+1) * 100 * p[j] + c[j]
				picked += p[j]

		if picked > maxPick:
			#print (i, " is un")
			continue
		#print ("i", i , "picked", picked, "point", point)

		# 残り個数分だけ、点数の高い問題をとる
		t = d-1
		while(picked < maxPick):
			if i & (2**t) != 0:
				t -= 1
				continue
			pick = min(p[t], (maxPick - picked))
			picked += pick
			point += (t+1)*100 * pick
			if pick == p[t]:
				point += c[t]
			#print ("t", t, "pick", pick, "picked", picked, "point", point)
			t -= 1

		if point >= g:
			return True
		else:
			pass
			#print (point)
	return False


def bin(d,g,p,c):
	left = 1
	right = sum(p)
	while left != right:
		cen = (left + right) // 2
		#print ("left", left, "cen", cen, "right", right)
		if(can(d,g,p,c,cen)):
			right = cen
		else:
			left = cen + 1
	return right


s = input().split(" ")
d = int(s[0])
g = int(s[1])

p = []
c = []

for i in range(0, d):
	s = input().split(" ")
	p.append(int(s[0]))
	c.append(int(s[1]))

print(bin(d,g,p,c))