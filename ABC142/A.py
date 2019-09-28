
N=float(input())

count=0
if(N%2==0):
    count=int(N/2)
else:
    count=int(N/2)+1

print(float(count/N))