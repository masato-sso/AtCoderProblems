
A, B, C, D, E, F, X = map(int, input().split())

takahashi = 0
aoki = 0
takahashiSetCount = int(X/(A + C))
takahashiModCount = X%(A + C)
aokiSetCount = int(X/(D + F))
aokiModCount = X%(D + F)

takahashi += takahashiSetCount * (A*B)
aoki += aokiSetCount * (D*E)

if(0 < takahashiModCount):
    if(A <= takahashiModCount):
        takahashi += A*B
    else:
        takahashi += takahashiModCount*B

if(0 < aokiModCount):
    if(D <= aokiModCount):
        aoki += D*E
    else:
        aoki += E*aokiModCount

if(takahashi == aoki):
    print("Draw")
elif(takahashi > aoki):
    print("Takahashi")
else:
    print("Aoki")