print('''
Digite o combustivel de sua preferencia
[01] Alcool
[02] Gasolina
[03] Diesel
[04] Fim
''')
qtd_alcool = 0
qtd_gasolina = 0
qtd_disel = 0
valor = 0


while valor !=4:
    valor=int(input())
    if valor ==1:
        qtd_alcool += 1
    if valor ==2:
        qtd_gasolina += 1
    if valor ==3:
        qtd_disel += 1
    if valor ==4:
        break

print(f'''
Muito Obrigado!
Alcool: {qtd_alcool}
Gasolina: {qtd_gasolina}
Disel: {qtd_disel}
''')
