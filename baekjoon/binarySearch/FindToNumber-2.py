import sys

def binary_search(i, n, start, end):
    if start > end:
        return (0)
    mid = (start + end) // 2
    if i == n[mid]:
        return (1)
    elif i < n[mid]:
        return (binary_search(i, n, start, mid-1))
    else:
        return (binary_search(i, n, mid+1, end))
    
a = int(input())
n = sorted(map(int, sys.stdin.readline().split()))
b = int(input())
m = map(int, sys.stdin.readline().split())
start = 0
end = len(n) - 1
for i in m:
    print(binary_search(i, n, start, end))
