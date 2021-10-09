
N,M = map(int, input().split())
num_player = 2*N
A = []
for i in range(num_player):
    A.append(input())
player = list(range(0,2*N))

# player1 judge
def judge(player1_hand, player2_hand):
    if(player1_hand == "G" and player2_hand == "G"):
        return -1
    elif(player1_hand == "G" and player2_hand == "C"):
        return 0
    elif(player1_hand == "G" and player2_hand == "P"):
        return 1
    elif(player1_hand == "C" and player2_hand == "G"):
        return 1
    elif(player1_hand == "C" and player2_hand == "C"):
        return -1
    elif(player1_hand == "C" and player2_hand == "P"):
        return 0
    elif(player1_hand == "P" and player2_hand == "G"):
        return 0
    elif(player1_hand == "P" and player2_hand == "C"):
        return 1
    elif(player1_hand == "P" and player2_hand == "P"):
        return -1

rank = [[0,i] for i in range(num_player)]
for round in range(M):
    for i in range(0,N):
        result = judge(A[rank[2*i][1]][round], A[rank[2*i+1][1]][round])
        if(result == -1):
            continue
        elif(result == 0):
            rank[2*i][0] -= 1
        else:
            rank[2*i+1][0] -= 1
    rank.sort()

for _,i in rank:
    print(i+1)