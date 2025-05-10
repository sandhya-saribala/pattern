rows=5
for r in range (1,rows+1):
    res=""
    for c in range(1,rows+1):
        res+=str(r)+" "
    print(res)


rows=5
for r in range(1,rows+1):
    res=""
    for c in range(1,r+1):
        res+=str(r)+' '
    print(res)
