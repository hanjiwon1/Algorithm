word = input()
number_dict = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
               '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
number = ''
for i in word:
    for j in range(2, 10):
        alpha = number_dict[str(j)]
        if alpha.count(i) == 1:
            number += str(j)
            break
sum = 0
for i in number:
    sum += int(i)+1
print(sum)
