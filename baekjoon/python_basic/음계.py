play_note = list(map(int, input().split()))
ascending = [1, 2, 3, 4, 5, 6, 7, 8]
print('ascending') if ascending == play_note else print('descending') if list(
    reversed(ascending)) == play_note else print('mixed')
