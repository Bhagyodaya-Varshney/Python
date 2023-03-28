str1=input("1:")
str2=input("2:")
b=""

for i in str1:
    if str2.count(i) == 0:
        b += i

print(b)