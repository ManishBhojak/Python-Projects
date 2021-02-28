#4 digit binary number divisible by 5
l1=[]
n=[x for x in input().split(',')]
for y in n:
    x=int(y,2)
    if not x%5:
        l1.append(y)
print(",".join(l1))
#Program Ended
