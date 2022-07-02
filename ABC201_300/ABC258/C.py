
N, Q = map(int, input().split())
S = input()
query = []
for i in range(Q):
    tmp = list(map(int, input().split()))
    query.append(tmp)

diff = 0
for q in query:
    op = q[0]
    if(op == 1):
        diff = diff + q[1]
        diff = diff % N
    else:
        idx = q[1] - 1
        print(S[(idx - diff)])

