def problema3():
    n = int(input())
    v1  = 1
    v2 = 1

    for i in range(n*2):
        print(f'{v1} {v1**2 + (i%2)} {v1**3 + (i%2)}')

    v1 += (i%2)
    v2 += (i+1)

problema3()
