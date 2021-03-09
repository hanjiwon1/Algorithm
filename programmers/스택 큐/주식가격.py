def solution(prices):
    answer = []
    prices_len = len(prices)
    for i in range(prices_len):
        num = prices[i]
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if num> prices[j]:
                answer.append(cnt)
                break
            if j == len(prices)-1:
                answer.append(cnt)
    answer.append(cnt)
    return answer

#print(solution(list(map(int, input().split()))))

 
