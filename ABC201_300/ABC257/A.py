
N, X = map(int, input().split())

string = ""
alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for alpha in alphas:
    string = string + (alpha)*N

ans = string[X - 1]

print(ans)