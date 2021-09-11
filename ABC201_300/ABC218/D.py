import itertools
 
N=int(input())
 
XY=[tuple(map(int,input().split())) for i in range(N)]
XY_set=set(XY)
 
points_can=itertools.combinations(XY,2)
 
ans=0
for point1,point2 in points_can:
    x1,y1=point1
    x2,y2=point2
 
    if(x1==x2 or y1==y2):
        continue
    if((x1,y2) in XY_set and (x2,y1) in XY_set):
        ans+=1
 
print(ans//2)