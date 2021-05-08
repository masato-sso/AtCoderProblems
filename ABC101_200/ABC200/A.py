
N=int(input())

cen=0
if(N%100==0):
    cen=int(N/100)
else:
    cen=int(N/100)+1

print(cen)