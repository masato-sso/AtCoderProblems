
S = []
for i in range(10):
    S.append(input())

A = -1
B = -1
C = -1
D = -1
for i in range(10):
    for j in range(10):
        s = S[i][j]
        if(s == "#"):
            if(A == -1):
                A = (i + 1)
            B = (i + 1)
            if(C == -1):
                C = (j + 1)
            D = (j + 1)

print("{} {}".format(A, B))
print("{} {}".format(C, D))
