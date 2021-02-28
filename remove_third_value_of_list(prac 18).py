#Remove and Print Every third number in list.
def remnum(l1):
    pos=3-1
    idx=0
    lenlis=(len(l1))
    while lenlis>0:
        idx=(pos+idx)%lenlis
        print(l1.pop(idx))
        lenlis-=1
l2=[10,20,30,40,50,60,70,80,90]
print("Remove and print every third number of list [10,20,30,40,50,60,70,80,90]: \n")
remnum(l2)
#Program Ended
