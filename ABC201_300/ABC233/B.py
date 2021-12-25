
L, R = map(int, input().split())
S = input()

L = L - 1
R = R - 1

start = S[:L]
sub = S[L:R + 1]
end = S[R + 1:]

print(start + sub[::-1] + end)