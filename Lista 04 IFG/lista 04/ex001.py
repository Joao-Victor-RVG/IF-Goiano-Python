def problema1():
    n = int(input())
    list = []
    d = 0
    f = 0
    for x in range(0 , n):
      list.append(int(input()))
    for x in list:
      if 10<=x<=20:
       d += 1
    else:
        f += 1
    print(f'{d} dentro')
    print(f'{f} fora')

problema1()              



