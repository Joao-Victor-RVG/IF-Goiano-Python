n = float(input('Digite um valor:\n'))

n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1
n1=float('%.2f'% n1)
n=float('%.2f'% n)

m50 = n // 0.5
n = n - m50*0.5
m50=float('%.2f'% m50)
n=float('%.2f'% n)

m25 = n // 0.25
n = n - m25*0.25
m25=float('%.2f'% m25)
n=float('%.2f'% n)

m10 = n // 0.10
n = n - m10*0.10
m10=float('%.2f'% m10)
n=float('%.2f'% n)

m5 = n // 0.05
n = n - m5*0.05
m5=float('%.2f'% m5)
n=float('%.2f'% n)

m1 = n * 100
m1=float('%.2f'% m1)
n=float('%.2f'% n)

print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')
print(f'{n1} nota(s) de R$ 1.00')

print('MOEDAS:')

print(f'{n1} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 1.00')
print(f'{m25} moeda(s) de R$ 1.00')
print(f'{m10} moeda(s) de R$ 1.00')
print(f'{m5} moeda(s) de R$ 1.00')
print(f'{m1} moeda(s) de R$ 1.00')

