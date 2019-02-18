# ABC001 B

m=float(input())
k=m/1000.0

VV=""
if k<0.1:
    VV="00"
elif k<=5.0:
    if k<1.0:
        k=k*10
        VV="0{}".format(int(k))
    else:
        VV=str(int(k*10))
elif 6.0<=k and k<=30:
    k=k+50
    VV=str(int(k))
elif 35<=k and k<=70:
    k=(k-30)/5+80
    VV=str(int(k))
elif 70<k:
    VV="89"

print(VV)