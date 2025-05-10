rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(1,i+1):
        res+=str(i)
    print(res)


rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i+j<=rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)

rows=4
mid=rows//2+1
for i in range (1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==2 or i==mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)