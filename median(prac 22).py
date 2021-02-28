#Python Program to find Median
x=int (input("Enter first value: "))
y=int(input("Enter Second value: "))
z=int(input("Enter Third value: "))
if x>y:
    if x<z:
        m=x
    elif y>z:
        m=y
    else:
        m=z
else:
    if x>z:
        m=x
    elif y<z:
        m=y
    else:
        m=z
print("After Processing ...")
print("Median of given Numbers: ",m)
#Program Ended
