
N = input()

str_len = len(N)

diff = 4 - str_len

if(diff == 0):
    print(N)
else:
    print("0"*diff + N)
