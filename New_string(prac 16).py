#Python Program to print new string with "Is"
def nstring(str):
    if len(str)>=2 and str[:2]=="Is":
        return str
    return "Is"+str
str=input("Enter a String: ")
print(nstring(str),"Is New String")
#Program Finished
