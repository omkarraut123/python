n = int(input())
n1 = n-1
l=list()

for i in range(n):
        
    row = list(map(int,input().split()))
    l.append(row[n1])
    n1-=1
print(sum(l))    