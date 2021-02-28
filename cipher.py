def enc(t,s):
    r=""

    for i in range(len(t)):
        char=t[i]

        if(char.isupper()):
            r=r+chr((ord(char)+s-65)%26+65)

        else:
                r=r+chr((ord(char)+s-97)%26+97)

    return r

t=input('Enter A Message: ')
s=4
print("Message: ",t)
print("Shifts: ",s)
print("Cipher: ",enc(t,s))
