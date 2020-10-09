import numpy as np
n=3
arr=np.array([[1,2,3],[2,3,4],[4,5,3]])
def spiral(arr,n):
    arr_l=list()
    i,k,l=0,0,0
    last_row,last_col=n-1,n-1
    while(k<=last_row and l<=last_col):
        for i in range(k,last_col+1):
            arr_l.append(arr[k,i])
        k+=1
        
        
        for i in range(k,last_row+1):
            arr_l.append(arr[i][last_col])
        last_col-=1    
        
        if(k<=last_row):
            for i in range(last_col,l-1,-1):
                arr_l.append(arr[last_row,i])
            last_row-=1 
           
        if(l<=last_col):
            for i in range(last_row,k-1,-1):
                arr_l.append(arr[i,l])
            l+=1    
    return arr_l        
           

arr_l=sorted(spiral(arr,n))

def spiral1(arr,arr_l,n):
    
    i,k,l=0,0,0
    j=0
    last_row,last_col=n-1,n-1
    while(k<=last_row and l<=last_col):
        for i in range(k,last_col+1):
            arr[k,i]=arr_l[j]
            j+=1
        k+=1
        
        
        for i in range(k,last_row+1):
            arr[i][last_col]=arr_l[j]
            j+=1
        last_col-=1    
        
        if(k<=last_row):
            for i in range(last_col,l-1,-1):
                arr[last_row,i]=arr_l[j]
                j+=1
                
                
            last_row-=1 
           
        if(l<=last_col):
            for i in range(last_row,k-1,-1):
                arr[i,l]=arr_l[j]
                j+=1
                
            l+=1    
    return arr 
    
print(spiral1(arr,arr_l,n))  