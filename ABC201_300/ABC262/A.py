
Y = int(input())

start = Y
ans = 0
for year in range(start, 3005):
    if(year%4 == 2):
        ans = year
        break

print(ans)