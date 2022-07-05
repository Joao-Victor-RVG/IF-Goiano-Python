c = int(input("cartas: "))
nipes = ['P', 'O', 'C', 'E']
qntd = {"P": 0, "O": 0, "C": 0, "E": 0}
msg_error = 'Numero informador é maior que a quantidade disponível'
print(f'Quantidade de cartas é {c}')
if c > 52:
    print("O Valor de cartas não pode ser maior que 52")
else:
    for i in range(len(nipes)):
        k = int(input(f"Quantidade de cartas igual a {nipes[i]}: "))
        if k < 14:
            if k <= c:
                qntd[nipes[i]] = k
                c = c - k
            else:
                print(msg_error)
                break
        else:
            print(msg_error)
            break
    print(qntd)
    print("Cartas faltantes:")
    for i in range(len(nipes)):
        print(f'{nipes[i]} = {13-qntd[nipes[i]]}')
        