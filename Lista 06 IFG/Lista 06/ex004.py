def problema4():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {'a': 300, 'b': 200, 'd':400}
    d3 = {
        "a":d1['a'] + d2['a'] , 
        "b":d1['b'] + d2['b'] ,
        "d":d2['d'],
        "c":d1['c']
    }
    print(d3)

problema4()


