
S=input()

even=[]
odd=[]

for i in range(len(S)):
    if((i+1)%2==0):
        even.append(S[i])
    else:
        odd.append(S[i])

odd_flag=True
for o in odd:
    if(o=="R" or o=="U" or o=="D"):
        pass
    else:
        odd_flag=False

even_flag=True
for e in even:
    if(e=="L" or e=="U" or e=="D"):
        pass
    else:
        even_flag=False


if(odd_flag and even_flag):
    print("Yes")
else:
    print("No")