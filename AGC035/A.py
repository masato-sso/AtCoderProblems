import numpy as np

size=input()
arr=np.array(input().split(" "),dtype=np.int32)

bit_array=[]
length_array=[]

for x in arr:
    bit_array.append(bin(x))
    length_array.append(len(bin(x)))

max_length=max(length_array)

fixed_bit_array=[]
for x,y in zip(bit_array,length_array):
    if y==max_length:
        fixed_bit_array.append(x[2:])
    else:
        pad=max_length-y
        x="{}{}".format("0"*pad,x[2:])
        fixed_bit_array.append(x)


result=[]
for i in range(max_length-2):
    count=0
    for x in fixed_bit_array:
        if x[i]=="1":
            count+=1
    if count%2==0:
        result.append("0")
    else:
        result.append("1")

if "1" in "".join(result):
    print("No")
else:
    print("Yes")

