str1=input("1:")
b=""

for i in str1:
    if str1.count(i) == 1:
        b += i

print(b)