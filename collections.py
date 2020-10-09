from collections import Counter
import heapq
arr=[1,2,6,5,6,5,5,3,3,4,1,1,1,6,5,8,8,6,6,6]
score=[100,500,300,400,455,251,454]
# use counter
counter=Counter(arr)
occur = counter.most_common(3)
print(occur)
# use heapq
print(heapq.nlargest(2,score))
print(heapq.nsmallest(2,score))