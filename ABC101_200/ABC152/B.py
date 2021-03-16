
ab=input().split(" ")
a=ab[0]
b=ab[1]

c1=""
for n in range(int(b)):
    c1=c1+a

c2=""
for n in range(int(a)):
    c2=c2+b

print(min(c1,c2))