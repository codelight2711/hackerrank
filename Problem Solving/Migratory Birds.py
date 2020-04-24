def migratoryBirds(arr):
    di={}
    for key in arr:
        if key in di.keys():
            di[key]+=1
        else:
            di[key]=1
    a=[]
    for value in di.values():
        a.append(value)
    maxi=max(a)
    a.clear()
    for val,count in di.items():
        if count==maxi:
            a.append(val)
    
    return min(a)
