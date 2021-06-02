from collections import deque
import sys
tc = int(input())
for _ in range(tc):
	n, m  = map(int, input().split())
	p = list(map(int, sys.stdin.readline().split()))
	doc = [0 for _ in range(n)]
	doc[m] = 1
	
	ret = 0
	while True:
		if p[0] == max(p):
			ret += 1
			if doc[0] != 1:
				del p[0]
				del doc[0]
			else:
				print(ret)
				break
		else:
			p.append(p.pop(0))
			doc.append(doc.pop(0))