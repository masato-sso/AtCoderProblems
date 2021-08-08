
H,W,N=map(int,input().split())

A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

a_dict={x:i+1 for i,x in enumerate(sorted(list(set(A))))}
b_dict={y:i+1 for i,y in enumerate(sorted(list(set(B))))}

for i in range(N):
    print(a_dict[A[i]],b_dict[B[i]])
