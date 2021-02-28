#Print Intersection of two lists
def inter(l1,l2):
    l3=[value for value in l1 if value in l2]
    return l3
l1=[4,9,1,17,11,15]
l2=[9,9,11,4,2,6]
print("Intersection of two Lists: ",inter(l1,l2))
#Program Ended
