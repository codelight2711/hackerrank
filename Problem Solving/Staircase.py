def staircase(n):
    c = n-1
    j = 1
    while c >= 0 and j <= n:
        print(c * ' '+ j * '#')
        j += 1
        c -= 1
