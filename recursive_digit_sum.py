def superDigit(n, k):
    # Write your code here
    if (len(str(n))!=1):
        m=list(str(n))
        r=[eval(i) for i in m]
        su=sum(r)
        su=su*k
       
        if (len(str(su))>1):
            return superDigit(su,1)
        else:
            return su
   
            
    else:
        return n
    