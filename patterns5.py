#print stars in centre of a square using patterns
rows=5
mid=rows//2+1
for r in range(1,rows+1):
    res=""
    for c in range (1,rows+1):
        if r==1 or r==rows or c==1 or c==rows or r==mid and c==mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)