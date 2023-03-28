string=input("Enter1:")
substring=input("Enter2:")
count=0
sublength=len(substring)
for i in range(0,(len(string)-sublength+1)):
        ##print(string[i:sublength+1])
        if string[i:sublength+i].upper()==substring.upper():
            count+=1
print(count)