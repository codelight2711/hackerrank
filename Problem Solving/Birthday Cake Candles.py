def birthdayCakeCandles(ar):  
    i=0
    count=0
    while i<len(ar)-1:
        if ar[i]>ar[i+1]:
            c=ar[i]
            ar[i]=ar[i+1]
            ar[i+1]=c
            i+=1
        else:
            i+=1
    max= ar[len(ar)-1]
    for element in ar:
        if element==max:
            count+=1
    return count
