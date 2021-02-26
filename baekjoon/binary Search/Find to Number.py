import sys
N = int(input())
arr_N = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr_M = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    print(int(arr_M[i] in arr_N))
