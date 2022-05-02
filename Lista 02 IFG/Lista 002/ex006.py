tempo = int(input('Quanto tempo você gastou em horas:\n'))
velmedia = int(input('Qual foi a sua velocidade media em km/h:\n'))
dist = tempo * velmedia
consumo = dist / 12 
print(f'{consumo:.3f}')



