
X=int(input())

changes=[500,100,50,10,5,1]

tmp=X
total=0

result=[]

result.append(int(tmp/500))

tmp=tmp%500

result.append(int(tmp/5))

total+=result[0]*1000
total+=result[1]*5

print(total)
