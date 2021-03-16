
N=int(input())
S=[]
total=0

for s in range(N):
    tmp=input()
    S.append("".join(sorted(tmp)))

S=sorted(S)
S_key=list(set(S))
count=[0]*len(S_key)
S_dict=dict(zip(S_key,count))


for s in S:
    total+=S_dict[s]
    S_dict[s]+=1

print(total)