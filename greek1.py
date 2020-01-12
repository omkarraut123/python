import heapq
score={'amit':95,
        'rahul':85,
         'nilesh':90,
         'john':88
       }
   
zip1=zip(score.keys(),score.values())       
zip2=zip(score.values(),score.keys()) 
print(sorted(zip1))
print(sorted(zip2))

print(score.keys())
print(score.values())

print("-----------------------------------------------------------------------------------------------------")
arr=[2,66,12,33,11,12]   
del arr[0]
print(arr)

arr.remove(66)
print(arr)

arr[-1] = "A random number"
print(arr) 

k = arr[:3] 
print(k)

if 33 in arr:
    print("33 is in array")
else:   
    print("33 not in array") 

print("-----------------------------------------------------------------------------------------------------")

arr2=[10,20,30,40,50]

def mul(*n):
    for i in n:
        return i*2

def multi_return(*num):
    n=num[0] 
    n1=num[1]  
    return n,n1  

result=list(map(mul,arr2))
print(result)  

print("-----------------------------------------------------------------------------------------------------")

arr=[int(i) for i in input("Enter elements : ").strip().split(' ')]
print(arr)
