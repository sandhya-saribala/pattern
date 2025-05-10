#print N using patern
rows=int(input("enter number of rows:"))
for r in range(1,rows+1):
    res=""
    for c in range(1,rows+1):
        if c==1 or c==rows or c==r:
           res+="@"+" "
        else:
            res+=" "+" "
    print(res)

#print Z using patterns
rows=int(input("enter number of rows:"))
for r in range(1,rows+1):
    res=""
    for c in range(1,rows+1):
        if r==1 or r==rows or r+c==rows+1:
            res+="$"+" "
        else:
            res+=" "+" "
    print(res)

#print R using pattern
rows=5
mid=rows//2+1
for r in range(1,rows+1):
    res=""
    for c in range (1,rows+1):
        if r<=mid:
            if r==1 or r==mid or c==1 or c==rows:
                res+= "&"+" "
            else:
                res+=" "+" "
        else:
            if c==1 or r==c:
                res+="&"+" "
            else:
                res+=" "+" "
    print(res)
        