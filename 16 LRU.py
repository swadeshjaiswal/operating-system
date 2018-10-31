arr=list(map(int,input('Enter the sequence seperated with space: \n').split()))
pageframe=[-1]*int(input('Frame size: '))
tracking=[0]*3
hit=0
fault=0
for i in range (len(arr)):
    if arr[i] in pageframe:
        hit+=1
        tracking[pageframe.index(arr[i])]=i+1
    if arr[i] not in pageframe:
        fault+=1
        pageframe[tracking.index(min(tracking))]=arr[i]
        tracking[pageframe.index(arr[i])] = i+1
print('Page faults: '+str(fault))
print('Page hits: '+str(hit))