
N=int(input())

S=0
for a in range(1,N+1):
    if(a%3==0 or a%5==0):
        continue
    else:
        S+=a

print(S)