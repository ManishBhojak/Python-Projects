#Checking Numbers are in Thousands are
def thousand(n):
    return ((abs(1000-n)<=100) or(abs(2000-n)<=100))
print("Find Numbers are in Thousands")
print(thousand(1000),"When Number = 1000")
print(thousand(900),"When Number = 900")
print(thousand(800),"When Number = 800")
print(thousand(2200),"When Number = 2200")
#Program Ended
