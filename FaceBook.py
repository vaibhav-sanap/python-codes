from sys import stdin
l = int(input())
n = int(input())
while(n>0):
    w,h = map(int,raw_input().strip().split(" "))
    if( w>=l and h>=l):
        if(w==h):
            print("ACCEPTED")
        else:
            print("CROP IT")
    else:
        print("UPLOAD ANOTHER")
    n=n-1    