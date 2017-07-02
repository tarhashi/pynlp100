f = open('hightemp.txt', 'r')
lines = len(f.readlines())
f.close()
print(lines)