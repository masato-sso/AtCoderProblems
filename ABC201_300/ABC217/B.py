
S=["ABC","ARC","AGC","AHC"]

S1=input()
S2=input()
S3=input()

input_s=[S1,S2,S3]

ans=""

for s in S:
    if(s in input_s):
        continue
    else:
        ans=s

print(ans)