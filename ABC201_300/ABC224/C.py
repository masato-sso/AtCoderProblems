
N = int(input())

X=[]
Y=[]
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)

ans = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            point1 = [X[i],Y[i]]
            point2 = [X[j],Y[j]]
            point3 = [X[k],Y[k]]

            if(((point2[0]-point1[0])*(point3[1]-point1[1])) != ((point3[0]-point1[0])*(point2[1]-point1[1]))):
                ans+=1

print(ans)
