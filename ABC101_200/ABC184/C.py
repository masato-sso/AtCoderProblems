
rc1=input().split(" ")
rc2=input().split(" ")

r1=int(rc1[0])
c1=int(rc1[1])
r2=int(rc2[0])
c2=int(rc2[1])

ans=0
if((r2-r1)==0 and (c2-c1)==0):
    ans=0
elif((r2-r1)==(c2-c1) or (r2-r1)==-(c2-c1)):
    ans=1
elif(abs(r2-r1)+abs(c2-c1)<=3):
    ans=1
elif(((r2-r1)^(c2-c1)^1)&1):
    ans=2
elif(abs(r2-r1)+abs(c2-c1)<=6):
    ans=2
elif(abs((r2-r1)+(c2-c1))<=3 or abs((r2-r1)-(c2-c1))<=3):
    ans=2
else:
    ans=3

print(ans)