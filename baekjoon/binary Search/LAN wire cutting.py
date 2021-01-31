import sys
K, N = map(int, input().split())
k_len = []

#k_len = list(map(int, sys.stdin.readlines()))
for i in range(K):
    k_len.append(int(input()))

min_len = 1
max_len = sum(k_len)//N

while min_len<=max_len:
    mid_len = (min_len+max_len)//2
    wire_cnt = sum([(i//mid_len) for i in k_len])
    if wire_cnt<N:
        max_len = mid_len-1
    elif wire_cnt >= N:
        min_len = mid_len+1
        re = mid_len


print(mid_len)
