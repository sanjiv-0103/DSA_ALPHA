def merge_sort(a,m,b,n):
    for i in range(n): #copying elements of b to a
        a[m+i]=b[i] 
    for i in range(m+n): #this loop is for sorting the arr a
        for j in range(i+1,m+n): #this loop is for comparing the elements of arr a
            if a[i]>a[j]: 
                a[i],a[j]=a[j],a[i] #swap 
    return a