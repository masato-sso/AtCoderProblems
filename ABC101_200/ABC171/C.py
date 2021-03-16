
N=int(input())

result=""
for i in range(1,99):
    if N<=pow(26,i):
        N=N-1
        for j in range(i):
            result+=chr(ord('a')+N%26)
            N=N//26
        break
    else:
        N=N-pow(26,i)

#print(div)
print(result[::-1])