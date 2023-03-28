n=input("Enter:")
pos=int(input("Enter position:"))
b=""
for i in range(0,len(n)):
    if i==pos-1:
        continue
    else:
        b=b+n[i]
print(b)