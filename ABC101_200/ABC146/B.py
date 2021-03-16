
N=int(input())
S=input()

w=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

result=""
for i in range(len(S)):
    idx=w.index(S[i])
    new_idx=(idx+N)%len(w)
    result=result+w[new_idx]

print(result)