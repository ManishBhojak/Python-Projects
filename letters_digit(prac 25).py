#Find letters and Digits in a String
nm=input("Input a Name: ")
d=0
l=0
for x in nm:
    if x.isdigit():
        d=d+1
    elif x.isalpha():
        l=l+1
    else:
        pass
print("Number of Letters in given String : ",l)
print("Number of Digits in given String : ",d)
#Program Ended

