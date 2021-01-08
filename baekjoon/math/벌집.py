n = int(input())
i = 0
sum = 1
while True:
    if n<=sum:
        print(i+1)
        break
    else:
        sum += 6*i+6
        i += 1
