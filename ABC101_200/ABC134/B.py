
S=input()

tmp=S.split()
N=int(tmp[0])
D=int(tmp[1])

result=float(N/(2*D+1))

if result-int(result)>0:
    result=int(result)+1
else:
    result=int(result)

print(result)
