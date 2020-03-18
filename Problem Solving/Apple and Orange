def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    q = []
    w = []
    u = []
    v = []
    i = 0
    k = 0
    for x in apples:
        q.append(x + a)
    for y in oranges:
        w.append(y + b)

    while i < len(q):
        if q[i] in range(s, t+1):
            u.append(q[i])
            i += 1
        else:
            i += 1

    while k < len(w):
        if w[k] in range(s, t+1):
            v.append(w[k])
            k += 1
        else:
            k += 1
    print(len(u))
    print(len(v))
