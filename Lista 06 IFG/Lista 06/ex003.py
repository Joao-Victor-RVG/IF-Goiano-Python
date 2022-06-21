def problema3():
    n=int(input())
    a = 1
    dic2={
        
    }
    for i in range(n):
        dic1 = {
            a: a*a
        }
        a=a+1
        dic1.update(dic2)
        dic2 = dict(dic1)
    print(dic2)

problema3()



