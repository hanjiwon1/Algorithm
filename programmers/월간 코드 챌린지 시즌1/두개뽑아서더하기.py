def solution(numbers):
    answer = set([])

    for i in numbers:
        for j in range(numbers.index(i)+1, len(numbers)):
            answer.add(i+numbers[j])
    answer = list(answer)
    answer.sort()
    return answer


#numbers = list(map(int, input().split()))
# print(solution(numbers))
