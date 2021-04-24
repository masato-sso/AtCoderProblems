
N=int(input())
S=input()
Q=int(input())

T=[]
A=[]
B=[]

for i in range(Q):
    t,a,b=map(int,input().split())
    T.append(t)
    A.append(a)
    B.append(b)

ans=S
str_list=list(ans)
all_swap_flag=False
for i,tidx in enumerate(T):
    if(tidx==1):
        a=A[i]
        b=B[i]
        if(all_swap_flag):
            if(a<N):
                a+=N
            else:
                a-=N
            if(b<N):
                b+=N
            else:
                b-=N
        
        tmp=str_list[a-1]
        str_list[a-1]=str_list[b-1]
        str_list[b-1]=tmp

    else:
        all_swap_flag=not all_swap_flag

if(all_swap_flag):
    tmp=str_list[:N]
    str_list[:N]=str_list[N:]
    str_list[N:]=tmp

print("".join(str_list))