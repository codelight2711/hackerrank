def diagonalDifference(arr):
    i = 0
    j = 0
    c = 0
    w = 0
    while i < len(arr) and j < len(arr):
        c = arr[i][j] + c
        w = arr[i][len(arr)-j-1] + w
        i = i + 1
        j = j + 1
    q=(abs(c-w))
    return(q)
