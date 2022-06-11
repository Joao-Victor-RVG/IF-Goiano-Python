from re import X
def problema2():
    matriz = []
    x = 0
    for c in range(0, 10):
       matriz.append(int(input()))
    for i in matriz:
       x += 1
    if i<0 or i ==0:
        i = 1 
    
    print(f'X[{x-1}] = {i}')

problema2()



