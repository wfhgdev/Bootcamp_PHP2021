def ascendente():
    l = [3,5,2,4,34,56,78,6,8,12,4,9]
    n = len(l)
    for i in range(n):
        e = l[i]
        a = i - 1
        while (e < l[a] and a >= 0):
            l[a+1] = l[a]
            a = a- 1
        l[a+1] = e
    print(l)

ascendente()