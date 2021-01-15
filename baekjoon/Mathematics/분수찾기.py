x = int(input())
# 홀수번째 대각선은 아래로, 짝수번째 대각선은 위로
# 각 대각선의 칸 수는 하나씩 늘어남
# 대각선 칸의 수는 등차수열을 이룸, 공차가 1, n
# 1  2  6  7  15 16 28 29 45
# 3  5  8  14 17 27 30 44
# 4  9  13 18 26 31 43
# 10 12 19 25 32 42
# 11 20 24 33 41
# 21 23 34 40
# 22 35 39
# 36 38
# 37
i = 1
while True:
    a = (2*i*i)  - (3*i) + 2
    b = (2*i*i) - i + 1
    a_ = (2*(i+1)*(i+1)) - (3*(i+1)) + 2
    #print('a, b, a_', a, b, a_)
    if x >= a and x < b:
        n = x-a
        denominator = 1+n
        molecule = (2*i-1)-n
        #print('if')
        break;
    elif x < a_ and x >= b:
        n = x-b
        denominator = (2*i) - n
        molecule = 1+n
        #print('elif')
        break;
    i += 1

print('%d/%d'% (molecule, denominator))
