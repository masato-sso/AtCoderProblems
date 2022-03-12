
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int, input().split())
    X.append(x)
    Y.append(y)

S = input()

left_max = {}
right_min = {}

collision = False
for i in range(N):
    if(S[i] == "R"):
        if(Y[i] in left_max and X[i] < left_max[Y[i]]):
            collision = True
    else:
        if(Y[i] in right_min and right_min[Y[i]] < X[i]):
            collision = True
    
    if(S[i] == "R"):
        if Y[i] in right_min:
            right_min[Y[i]] = min(X[i], right_min[Y[i]])
        else:
            right_min[Y[i]] = X[i]
    else:
        if Y[i] in left_max:
            left_max[Y[i]] = max(X[i], left_max[Y[i]])
        else:
            left_max[Y[i]] = X[i]

if(collision):
    print("Yes")
else:
    print("No")
