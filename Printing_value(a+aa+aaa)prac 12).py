#printing the value of a+aa+aaa
a=int (input ("Enter value: "))

n1=int("%s"%a) #n1 is value is a
n2=int("%s %s "%(a,a)) #n2 value is a*a
n3=int ("%s %s %s"%(a,a,a))#n3 value is a*a*a
print("n1=a, n2=a*a, n3=a*a*a")
print("Result of a+aa+aaa: ",n1+n2+n3)
#Program Ended
