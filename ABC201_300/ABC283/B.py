
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = []
for i in range(Q):
    queries.append(list(map(int, input().split())))

for q in queries:
    opt = q[0]
    k = q[1] - 1
    if(opt == 1):
        A[k] = q[2]
    else:
        print(A[k])
