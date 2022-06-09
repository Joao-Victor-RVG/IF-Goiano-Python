n = int(input())

for i in range(n):
    p1 = input()
    p1 = p1.split(' ')
    p1 = p1[0]
    p2 = input()
    p2 = p2.split(' ')
    p2 = p2[0]

    if p1 == 'ataque':
        if p2 == 'ataque':
            print('Aniquilacao mutua')
        elif p2 == 'pedra':
            print('Jogador 1 venceu')
        else:
            print('Jogador 1 venceu')
    elif p1 == 'pedra':
        if p2 == 'ataque':
            print('Jogador 2 venceu')
        elif p2 == 'pedra':
            print('Sem ganhador')
        else:
            print('Jogador 1 venceu')
    elif p1 == 'papel':
        if p2 == 'ataque':
            print('Jogador 2 venceu')
        elif p2 == 'pedra':
            print('Jogador 2 venceu')
        else:
            print('Ambos venceram')



