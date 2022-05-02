age = int(input('digite um valor inteiro correspondente a sua idade:\n'))

a = age // 365
age = age - a*365

m = age // 30
age = age - m*30

d = age

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))

