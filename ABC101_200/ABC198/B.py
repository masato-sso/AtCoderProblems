
N=input()

reverse_N=N[::-1]

zero_count=0

for s in reverse_N:
    if(s=="0"):
        zero_count+=1
    else:
        break

eval_N="0"*zero_count+N

yes_flag=True
length=len(eval_N)
for idx in range(0,int(length/2)):
    if(eval_N[idx]==eval_N[length-1-idx]):
        continue
    else:
        yes_flag=False
        break

if(yes_flag):
    print("Yes")
else:
    print("No")