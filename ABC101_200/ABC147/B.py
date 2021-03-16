
s=input()

le=len(s)
count=0

for i in range(int(le/2)):
    if(s[i]!=s[le-1-i]):
        count+=1

print(count)          