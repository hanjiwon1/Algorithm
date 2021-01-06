Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in Croatia:
    a = a.replace(i, 'a')
print(len(a))
