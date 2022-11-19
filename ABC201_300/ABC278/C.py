
N, Q = map(int, input().split())
T = []
A = []
B = []
for q in range(Q):
    t, a, b = map(int, input().split())
    T.append(t)
    A.append(a)
    B.append(b)

follows = set()

for i in range(Q):
    t = T[i]
    a = A[i]
    b = B[i]
    if(t == 1):
        follows.add((a,b))
    elif(t == 2):
        try:
            follows.remove((a,b))
        except:
            pass
        continue
    elif(t == 3):
        if((a,b) in follows and (b, a) in follows):
            print("Yes")
            continue
        print("No")
