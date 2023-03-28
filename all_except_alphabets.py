n=input("Enter:")
b=" "
for i in n:
    if i.isalpha() or i.isspace():
        b+=i
print(b)