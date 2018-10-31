arr=list(map(int,input().split()))
pageframe=[-1]*int(input())
hit=0
fault=0
pf=0
for i in range (len(arr)):
    if arr[i] in pageframe:
        hit+=1
    if arr[i] not in pageframe:
        fault+=1
        if pf>(len(pageframe)-1):
            pf=0
        pageframe[pf]=arr[i]
        pf+=1

print('hit is '+str(hit))
print("fault is "+ str(fault))
