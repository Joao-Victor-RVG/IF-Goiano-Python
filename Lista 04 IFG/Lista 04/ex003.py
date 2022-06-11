def problema3():
    n = input().split(' ')
    n.reverse()
    for i in range(len(n)):
       print(f'X[{i}] = {n[i]}')
problema3()
