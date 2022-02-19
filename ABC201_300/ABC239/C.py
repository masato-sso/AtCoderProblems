
x1,y1,x2,y2 = map(int, input().split())

def candidate_5(px, py):
    points = [(px-2, py-1), (px-1, py-2), (px+1, py-2), (px+2, py-1), (px+1, py+2), (px+2, py+1), (px-2, py+1), (px-1, py+2)]
    return points

cans1 = candidate_5(x1, y1)
cans2 = candidate_5(x2, y2)

ans = 0
for can in cans1:
    if (can in cans2):
        ans+=1

if (ans > 0):
    print("Yes")
else:
    print("No")