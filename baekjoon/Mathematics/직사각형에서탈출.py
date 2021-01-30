x, y, w, h = map(int, input().split())
short_x = w-x if x > w-x else x
short_y = h-y if y > h-y else y
print(short_x) if short_x < short_y else print(short_y)

# print(min(x, y, w-x, h-y))
