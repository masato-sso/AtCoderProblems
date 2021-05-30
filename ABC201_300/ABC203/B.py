
N,K=map(int,input().split())

rooms=[]
for i in range(1,N+1):
    for j in range(1,K+1):
        rooms.append(int("{}0{}".format(i,j)))

print(sum(rooms))