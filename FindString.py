t = int(raw_input())
for i in range(t):
    arr = [int(j) for j in raw_input().split()]
    stringarr = []
    lenoflist=0
    for j in range(arr[0]):
        stringarr.append(raw_input())
        lenoflist = lenoflist+1
        
    givenstr = raw_input()

    var = 0
    k = 0
    for j in range(0, len(givenstr)):
        if (givenstr[j] in stringarr[ j-k*lenoflist]):
            var = 1
        else:
            var = 0
            break    
        if(j==(k+1)*lenoflist-1):
            k = k+1

    if(var == 0):
        print ("No")
    else:
        print ("Yes")  