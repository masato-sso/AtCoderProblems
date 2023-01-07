
T = int(input())

tests = []
result = []
for i in range(T):
    tmp = input()
    array = list(map(int, input().split()))
    ans = 0
    for a in array:
        if(a%2 == 0):
            continue
        ans += 1
    result.append(ans)

for r in result:
    print(r)