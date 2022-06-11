
R,C = map(int, input().split())
A = []
for i in range(2):
    tmp = list(map(int, input().split()))
    A.append(tmp)

print(A[R-1][C-1])