st = 'python programming'
for i in range(len(st)):
    if i%2 == 0:
        print(st[i].upper(),end='-')
    else:
        print(st[i],end = '-')
    