from math import gcd
#numpyよりmathの方が速い
 
K=int(input())
 
S=0
for a in range(1,K+1):
    for b in range(1,K+1):
        calc=gcd(a,b)
        for c in range(1,K+1):
                S+=gcd(calc,c)
 
print(S)