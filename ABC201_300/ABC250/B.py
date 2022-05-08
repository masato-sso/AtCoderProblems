
N, A, B = map(int, input().split())

block = ""
reverseBlock = ""
blockColor = "."
reverseBlockColor = "#"

for i in range(A):
    for j in range(N):
        if(j%2 == 0):
            blockColor = "."*B
            reverseBlockColor = "#"*B
        else:
            blockColor = "#"*B
            reverseBlockColor = "."*B
        block += blockColor
        reverseBlock += reverseBlockColor
    if(i == (A - 1)):
        continue
    block += "\n"
    reverseBlock += "\n"

ans = ""
for i in range(N):
    if(i%2 == 0):
        ans += block
    else:
        ans += reverseBlock
    ans += "\n"

print(ans)
