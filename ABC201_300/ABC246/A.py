from collections import Counter

x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

x = [x1, x2, x3]
y = [y1, y2, y3]

cx = Counter(x)
cy = Counter(y)

xKey = cx.keys()
yKey = cy.keys()

ansX = 0
for key in xKey:
    cnt = cx[key]
    if(cnt != 2):
        ansX = key

ansY = 0
for key in yKey:
    cnt = cy[key]
    if(cnt != 2):
        ansY = key

print("{} {}".format(ansX, ansY))
