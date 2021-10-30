
S = input()

cans = []
cans.append(S)
cans.append(S[0]+S[2]+S[1])
cans.append(S[1]+S[0]+S[2])
cans.append(S[1]+S[2]+S[0])
cans.append(S[2]+S[0]+S[1])
cans.append(S[2]+S[1]+S[0])

print(len(list(set(cans))))