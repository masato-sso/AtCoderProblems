
X, K = map(int, input().split())

pow10 = 1
for i in range(K):
    X = X/pow10
    m = (X%10)
    if(m <= 4):
        X -= m
    else:
        X += (10 - m)
    X *= pow10
    pow10 *= 10

print(int(X))