import numpy as np

N=int(input())
H=np.array(input().split(),dtype=np.int32)

reverseH=H[::-1]

move_count=0
max_move=0

for i in range(N-1):
    if(reverseH[i]<=reverseH[i+1]):
        move_count+=1
        if(max_move<move_count):
            max_move=move_count
    else:
        move_count=0

print(max_move)

