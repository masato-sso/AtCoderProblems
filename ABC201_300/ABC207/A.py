
A,B,C=map(int,input().split())

a=[A,B,C]

ra=sorted(a)[::-1]

print(ra[0]+ra[1])