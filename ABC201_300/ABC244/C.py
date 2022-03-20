
N = int(input())
hands = list(range(1, 2*N + 2))

while(True):
    print(hands[0])
    hands.remove(hands[0])
    n = int(input())
    if(n == 0):
        break
    hands.remove(n)
