#print long string in list & words and frequencies
w='''In botany, a tree is a perennial plant'''
wl=w.split()
wf=[wl.count(n) for n in wl]
print("Printing list of Given long String")
print("List: \n",str(wl))
print("Printing Given long String words & frequency")
print("Words and Frequencies: \n",str(list(zip(wl,wf))))
#Program Ended
