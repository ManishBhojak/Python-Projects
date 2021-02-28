#Check Validity of a Password
import re
p=input("Enter your Password ")
x=True
while x:
    if(len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Password you enter have [a-z],[A-Z],[0-9],[$#@] so, it is valid Password")
        x=False
        break
    if x:
        print("Password does not contain [a-z],[A-Z],[0-9],[$#@] so, it is invalid Password")
#Program Ended
