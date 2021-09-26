
K=int(input())
A,B=map(str,input().split())

A_base10=0
k=1
for a in A[::-1]:
    A_base10=A_base10+k*int(a)
    k=k*K

B_base10=0
k=1
for b in B[::-1]:
    B_base10=B_base10+k*int(b)
    k=k*K

print(A_base10*B_base10)