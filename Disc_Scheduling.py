import matplotlib.pyplot as plt
print('Enter the sequence with space in between'
      ' elements: ')
arr=list(map(int,input().split()))
length=1
print('Initial head position:')
head=int(input())
arrhead=list()
arrhead.append(head)
count=0
for _ in range (len(arr)):
    lowl=list()
    for i in arr:
        lowl.append(abs(head-i))
    llow=min(lowl)
    head=arr[lowl.index(min(lowl))]
    length+=1
    arrhead.append(head)
    count +=abs(llow)
    arr.remove(head)
print('Total seek count ='+str(count))
print('head positions are:')
print(*arrhead,sep=' ')
y=list()
for i in range(length):
    y.append(i+1)
plt.plot(arrhead,y)
plt.scatter(arrhead,y)
plt.show()