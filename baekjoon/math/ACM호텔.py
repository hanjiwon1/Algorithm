for i in range(int(input())):
    h, w, n = map(int, input().split())
    guest_h = n
    cnt = 1
    while guest_h>h:
        guest_h -= h
        cnt += 1
    print(str(guest_h)+str(cnt).zfill(2))
