arr = list(map(int,input().split()))
minsum=None
minindex=0
l=len(arr)
for i in range(1,l-1):
    if(minsum == None):
        minsum = abs(sum(arr[:i]) - sum(arr[i+1:]))
        minindex = i
    else:
        minsum_new = abs(sum(arr[:i]) - sum(arr[i+1:]))
        if(minsum_new<minsum):
            minsum = minsum_new
            minindex = i
print("min index of sum difference is : ",minindex)        
        
    