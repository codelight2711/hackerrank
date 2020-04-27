def miniMaxSum(arr):
    arr.sort()
    i = 1
    c=0
    d=0
    n=len(arr)-2
    while i < len(arr) and n>=0:
        c += arr[i]
        i += 1
        d += arr[n]
        n -= 1

    print(d,c)
