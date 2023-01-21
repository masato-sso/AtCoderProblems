
N, P, Q, R, S = map(int, input().split())
A = list(map(str, input().split()))

tmp = A[P-1:Q]
B = A

B[P-1:Q] = A[R-1:S]
B[R-1:S] = tmp

print(" ".join(B))