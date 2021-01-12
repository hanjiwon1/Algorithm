n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(input())
min = 50
for i in range(m-8+1):
    for j in range(n-8+1):
        x, y = i, j
        fir = 'B'
        sec = 'W'
        cnt = 0
        while True:
            #print(x, y)
            if x%2 == 0:
                if board[y][x] != fir: cnt += 1
            else:
                if board[y][x] != sec: cnt += 1
            x += 1
            if x == i+8:
                x = i
                y += 1
                fir, sec = sec, fir
                if y == j+8: break
        if min>cnt: min = cnt
        cnt = 0
        x = i
        y = j
        fir = 'W'
        sec = 'B'
        while True:
            if x%2 == 0:
                if board[y][x] != fir: cnt += 1
            else:
                if board[y][x] != sec: cnt += 1
            x += 1
            if x == i+8:
                x = i
                y += 1
                fir, sec = sec, fir
                if y == j+8: break
        if min>cnt: min = cnt

print(min)


