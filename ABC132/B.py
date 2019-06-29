import numpy as np

size=input()
P=input()

p=P.split(" ")
p=np.array(p,dtype=np.int32)

counter=0

for i in range(0,len(p)-2):
    if(p[i]<p[i+1] and p[i+1]<p[i+2]):
        counter+=1
    elif(p[i]>p[i+1] and p[i+1]>p[i+2]):
        counter+=1

print(counter)