
S=input()

odd_s=[]
even_s=[]

for i in range(len(S)):
    num=i+1
    if(num%2==0):
        even_s.append(S[i])
    else:
        odd_s.append(S[i])

odd="".join(odd_s)
even="".join(even_s)

if(len(odd)==1):
    if(odd.islower()):
        print("Yes")
    else:
        print("No")
else:
    if(odd.islower() and even.isupper()):
        print("Yes")
    else:
        print("No")