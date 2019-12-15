def bubbleSort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
        print(list)            

            
    return list        


list=[55,12,33,5,0,9,66,5,6,7]
bubbleSort(list)
print(list)
