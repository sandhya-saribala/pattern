a=0
b=1
count=0
while a<=500:
    print(a)
    count+=1
    c=a+b
    a=b
    b=c
print("total fibonacci numbers between 0 and 500:",count)