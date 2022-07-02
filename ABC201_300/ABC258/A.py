
K = int(input())

hour = int(K / 60)
minutes = K % 60

time = "{:0>2}:{:0>2}".format(21 + hour, 0 + minutes)

print(time)