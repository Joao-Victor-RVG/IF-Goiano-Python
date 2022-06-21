def problema2():
    dic = {
    1:10, 
    2:20, 
    3:30, 
    4:40, 
    5:50, 
    6:60
}

    key = int(input(''))

    if dic.get(key):
      print('A chave {} está presente no dicionário'.format(key))
    else:
        print('A chave {} não está presente no dicionário'.format(key))



problema2()       