from itertools import combinations

N, M = map(int, input().split())

comb_list = combinations(range(1, M + 1), N)

for comb in comb_list:
    ans = ""
    for c in comb:
        ans = ans + str(c)
        ans = ans + " "
    ans = ans[:-1]
    print(ans)