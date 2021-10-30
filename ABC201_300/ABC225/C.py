
N,M = map(int,input().split())

B = []
for i in range(N):
    B.append(list(map(int,input().split())))

X = []
Y = []
for i in range(N):
    x = []
    y = []
    for j in range(M):
        x.append((B[i][j]+6)/7)
        y.append((B[i][j]-1)%7+1)
    X.append(x)
    Y.append(y)

ans = "Yes"
for i in range(N):
    for j in range(M):
        if(0<i and X[i][j]!=X[i-1][j]+1):
            ans = "No"
        if(0<j and Y[i][j]!=Y[i][j-1]+1):
            ans = "No"

print(ans)
