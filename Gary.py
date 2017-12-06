from sys import stdin
n,q=map(int,raw_input().strip().split(" "))
arr=map(int,raw_input().strip().split(" "))

while(q):
    ty,x,y = map(int,raw_input().strip().split(" "))
    if(ty==1):
        arr[x] = y
    else:
        sum=0
        for i in range(x,y+1):
            sum =sum+arr[i]
        print(sum)
          
    q=q-1
