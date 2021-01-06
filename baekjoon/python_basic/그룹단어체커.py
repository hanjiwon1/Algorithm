n = int(input())
cnt = 0
for i in range(n):
    word = input()
    simple_word = word[0]
    for j in word:
        if simple_word[len(simple_word)-1] != j:
            simple_word += j
    if len(set(simple_word)) == len(simple_word):
        cnt += 1
print(cnt)
