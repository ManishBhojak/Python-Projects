#Print Factorial of given number
n=int(input("Enter a number: "))
f=1
if n<0:
    print("Sorry, Invalid Entry")
elif n==0:
    print("Factorial : 1")
else:
    for i in range(1,n+1,1):
        f=f*i
        print("Factorial of ",n,"is ",f)
#Program Ended
          
