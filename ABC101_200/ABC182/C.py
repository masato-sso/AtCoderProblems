import numpy as np

N=input()

K=len(N)

keta_list=list(N)

def power_set(item_lists):
    p_sets = [[]]
    for item in item_lists:
        tmp = []
        for element in p_sets:
            tmp.append(element + [item])
        p_sets.extend(tmp)
    return p_sets

num_list=power_set(keta_list)

nums=[]
for num in num_list:
    if(len(num)==0):
        continue
    else:
        n=int("".join(num))
        nums.append(n)

nums=sorted(nums)[::-1]

ans=-1
for n in nums:
    if(n%3==0):
        ans=K-len(str(n))
        break

print(ans)