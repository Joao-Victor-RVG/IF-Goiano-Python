def tabuleiro(h, w):
  for i in range(h):
    for i in range(0, w):
      print('.#', end="")
    print('')
tab = input().split(' ')
h = int(tab[0])
w = int(tab[1])


tabuleiro(h, w)

