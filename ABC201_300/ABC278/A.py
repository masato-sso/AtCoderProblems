
N, K = map(int, input().split())
A = list(map(str, input().split()))

for i in range(K):
    A.pop(0)
    A.append("0")

ans = " ".join(A)
print(ans)