from re import X


def problema2():
    for i in range(10):
        entrada = int(input())
        if entrada <= 0:
            X.insert(i , 1)
        else:
            X.insert(i , entrada)
        print(f'X[{i}] = {X[i]}')


x = []
problema2(X)




