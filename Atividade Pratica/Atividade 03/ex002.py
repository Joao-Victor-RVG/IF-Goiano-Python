#Atividade prática do dia 04/07/2022

input_num = int(input(""))
list = [] 
for n in range(input_num):
    list.append([])
    list[n].append(1)
    for m in range(1, n):
        list[n].append(list[n - 1][m - 1] + list[n - 1][m])
    if(input_num != 0):
        list[n].append(1)
for n in range(input_num):
    print(" " * (input_num - n), end = " ", sep = " ")
    for m in range(0, n + 1):
        print('{0:5}'.format(list[n][m]), end = " ", sep = " ")
    print()



