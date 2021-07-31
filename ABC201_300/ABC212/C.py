
N,M=map(int,input().split())
A=sorted(list(map(int,input().split())))
B=sorted(list(map(int,input().split())))

MAX=10000000000

cans_diff=MAX

i=0
j=0
while(True):
    if(i<N and j<M):
        cans_diff=min(cans_diff,abs(A[i]-B[j]))
        if(A[i]>B[j]):
            j+=1
        else:
            i+=1
    else:
        break

print(cans_diff)