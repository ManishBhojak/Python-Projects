#Sort a list in Ascending and Descending order
l1=[5,2,8,7,1]
temp=0
print("Original List")
for i in range (0,len(l1),1):
    print(l1[i],end=" ")
for j in range(i+1,len(l1),1):
    if(l1[i]>l1[j]):
        temp=l1[i]
        l1[i]=l1[j]
        l1[j]=temp
print()
print("Element of list in Ascending : ")
for i in range (0,len(l1),1):
    print(l1[i],end=" ")
for i in range (0,len(l1),1):
    print(l1[i],end=" ")
for j in range(i+1,len(l1),1):
    if(l1[i]<l1[j]):
        temp=l1[i]
        l1[i]=l1[j]
        l1[j]=temp
print("Element of list in Descending : ")
for i in range (0,len(l1),1):
    print(l1[i],end=" ")
#Program Ended
