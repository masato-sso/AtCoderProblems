
X, Y, Z = map(int, input().split())

if(Y < 0):
    X = -X
    Y = -Y
    Z = -Z

if(X < Y):
    print(abs(X))
else:
    if(Y < Z):
        print(-1)
        exit(0)
    else:
        print(abs(Z) + abs(X - Z))
