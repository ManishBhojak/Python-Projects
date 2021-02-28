#Add Two Numbers without + operator
def add(a,b):
    while b!=0:
        c=a&b
        a=a^b
        b=c<<1
    return a
print("Addiction of two number a=5 and b=6 without + operator = ",add(5,6))
#Program Ended
