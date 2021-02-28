#Max and Min values and Min-Max Index of the List
def ind(a,n):
    mini=a.index(min(a))
    maxi=a.index(max(a))
    print("Maximum Index : ",maxi+1)
    print("Minimum Index : ",mini+1)
a=[8,1,7,10,5]
mine=a[0]
maxe=a[0]
for i in range(1,len(a),1):
    if a[i]<mine:
        mine=a[i]
    if a[i]>maxe:
        maxe=a[i]
print("Minimum Element Of List : ",mine)
print("Maximum Element Of List : ",maxe)
#Program Ended
