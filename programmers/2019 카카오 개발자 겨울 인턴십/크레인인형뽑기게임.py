def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(basket) == 0: basket.append(board[j][i-1])
                elif basket[-1] == board[j][i-1]:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(board[j][i-1])
                board[j][i-1] = 0
                break

                
            
    return answer

'''
board = []
moves = []

n = int(input())

for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

moves = list(map(int, input().split()))
print(solution(board, moves))
'''
