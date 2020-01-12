pos=[]
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True

        i+=1
    return False

list=[45,20,11,45,44,44]   
n=int(input("Enter element to search : "))
if search(list,n):
    print("found at position=%d"%int(pos+1)) 
else:
    print("not found")    