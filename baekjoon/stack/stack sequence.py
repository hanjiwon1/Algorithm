import sys
n = int(input())
ar = list(range(1, n+1))
seq = []


# seq = list(map(int, sys.stdin.readlines()))
for i in range(n):
    seq.append(int(input()))

i = 0
j = 0
k = 0
stack = []
p = []
while j <= n-1:
    stack.append(ar[j])
    p.append('+')

    while stack[i] == seq[k]:
        p.append('-')
        stack.pop()
        i -= 1
        k += 1
        if i == -1: break
    j += 1
    i += 1

if len(stack) != 0:
    print('NO')
else:
    print(*p, sep='\n')
