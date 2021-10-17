
S = input()

s_list = list(S)

cans = []

target = s_list
for i in range(len(s_list)):
    val = target.pop(0)
    target.append(val)
    cans.append("".join(target))

result = sorted(cans)

print(result[0])
print(result[-1])
