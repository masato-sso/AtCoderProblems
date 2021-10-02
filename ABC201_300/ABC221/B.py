
S = input()
T = input()

s_comp = list(S)
length = len(s_comp)
cans=[]
cans.append(S)
for i in range(1,length):
    s_comp = list(S)
    tmp = s_comp[i-1]
    s_comp[i-1] = s_comp[i]
    s_comp[i] = tmp
    cans.append("".join(s_comp))

if(T in cans):
    print("Yes")
else:
    print("No")
