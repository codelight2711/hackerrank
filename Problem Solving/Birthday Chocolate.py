def birthday(s, d, m):
    ans=0
    for i in range(len(s)):
        n=0
        count=0
        while(n<(m)):
            count+=s[i+n]
            n+=1
        if(count==d):
            ans+=1
        if(i+n==len(s)):
            break
            
    return ans
