pos=-1 # global variable

def search(list,n):
    i=0

    while i<len(list):
        if (list[i]==n):
            globals()['pos']=i
            return True
            
        i=i+1
    return False

list=[2,3,4,8,9,5]
n=int(input("Enter number for search"))
if(search(list,n)):
    print("Fount at position",pos+1)
else:
    print("Not Fount")

