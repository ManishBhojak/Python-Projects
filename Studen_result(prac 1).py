#find the total marks and percentage of student with grade of five subjects
h=int(input("Enter Hindi Marks: "))
e=int(input("Enter English Marks: "))
m=int(input("Enter Maths Marks: "))
sc=int(input("Enter Science Marks: "))
ss=int(input("Enter SST Marks: "))
t=h+e+m+sc+ss
print('Total Marks : ',t)
p=t/5
print("Percentage : ",p)
if p<50:
    print("Grade C")
elif p<80:
    print("Grade B")
else:
    print("Grade A")
#Program Ended
