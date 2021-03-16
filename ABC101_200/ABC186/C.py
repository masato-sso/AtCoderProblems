
N=int(input())

hit=0
for n in range(1,N+1):
    if("7" in str(n)):
        hit+=1
    elif("7" in str(oct(n))):
        hit+=1

ans=N-hit
print(ans)