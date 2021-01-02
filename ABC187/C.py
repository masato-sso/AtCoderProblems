
N=int(input())

S=[]
non_keys=[]
ex_keys=[]
for i in range(N):
    s=input()
    if("!" in s):
        ex_keys.append(s.replace("!",""))
    else:
        non_keys.append(s)



non_keys=sorted(list(set(non_keys)))
ex_keys=sorted(list(set(ex_keys)))
sat_flag=True
ans=""

keys={}
for k in non_keys:
    keys[k]=0
for e in ex_keys:
    keys[e.replace("!","")]=0

for n in non_keys:
    keys[n]+=1

for n in ex_keys:
    keys[n]+=1

KEY=keys.keys()
for k in KEY:
    if(keys[k]>=2):
        ans=k
        sat_flag=False
    
if(sat_flag):
    print("satisfiable")
else:
    print(ans)