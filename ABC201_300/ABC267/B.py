
S = input()

if(S[0] == "0"):
    rows = []
    if(S[6] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    if(S[3] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    if(S[7] == "0" and S[1] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    if(S[4] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    if(S[8] == "0" and S[2] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    if(S[5] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    if(S[9] == "0"):
        rows.append(0)
    else:
        rows.append(1)
    check = False
    startOneIdx = -1
    endOneIdx = -1
    for idx in range(len(rows)):
        r = rows[idx]
        if(r):
            endOneIdx = idx
    for idx in range(len(rows)):
        r = rows[idx]
        if(r):
            startOneIdx = idx
            break
    if(startOneIdx == -1 or endOneIdx == -1):
        print("No")
        exit(0)
    for idx in range(startOneIdx, endOneIdx + 1):
        r = rows[idx]
        if(r == 0):
            check = True
            break
    if(check):
        print("Yes")
    else:
        print("No")
else:
    print("No")