
X = float(input())

intX = int(X)
powX = X*1000

diff = powX-intX*1000
if(diff >= 500):
    print(intX+1)
else:
    print(intX)
