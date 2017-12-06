from sys import stdin
n   = int(input())
arr = map(int,raw_input().strip().split(" "))
product=1
for i in range(0,n):
    product = (product*arr[i])%1000000007
print(product)


