import sys

a = int(input())
n = set(sys.stdin.readline().split())
b = int(input())
m = sys.stdin.readline().split()
for i in m:
	print('1') if i in n else print('0')
