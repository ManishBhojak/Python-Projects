#Python program to get list of packages in python
import pkg_resources
packages=pkg_resources.workingset
packages_list=sorted(["%S ==%S"%(i.key,i.version) for i in packages])
print("Printing  Python Packages list: ")
for m in packages list:
    print(m)
#Program Ended
