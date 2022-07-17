
N, X, Y = map(int, input().split())

R = [0]*12
B = [0]*12

R[1] = 0
B[1] = 1

for n in range(2, N + 1):
    B[n] = R[n - 1] + B[n - 1] * Y
    R[n] = R[n - 1] + B[n] * X

print(R[N])