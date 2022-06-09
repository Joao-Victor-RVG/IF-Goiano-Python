def problema4():
    x = 100
    soma = 0
i = 0
while x >= 0:
    x = int(input())
    if x >= 0:
        i = i + 1
        soma = soma + x
media = soma / i
print(f'{media:.2f}')

problema4()



