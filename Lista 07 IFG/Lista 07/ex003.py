#Questão 1186
matriz = []
tipo = input()
for i in range(12):
    linha = []
    for j in range(12):
        num = input()
        linha.append(float(num))
    matriz.append(linha)
matriz_F = []
a = 11
b = 1 
aux = 1
while a >= 1:
    
    while b <= 11:
        matriz_F.append(matriz[a][b])
        b+=1
    aux +=1     
    a -= 1
    b = aux
    
if tipo == "S":    
    print(sum(matriz_F))
elif tipo == "M":
    print("%.1f"%(sum(matriz_F)/66))



    