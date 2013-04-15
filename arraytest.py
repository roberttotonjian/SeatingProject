master = [None] * 100
print master[5]
for i in range(100):
	j = i*i
	master[i] = [j, j+1, j+2]

for x in range(10):
	print master[x][2]
	print master[x][1]


user = [[1110, 'Adam'], [1111, 'Toto'], [1112, 'Rodney'], [1113, 'Jon']]
comp = [[1110, 1], [1111, 4], [1112, 3], [1113, 3]]
seat = [[1110, 0, 0], [1111, 0, 1], [1112, 0, 2], [1113, 1, 0]]
complist = [[0, 'Earlier Crap'], [1, 'Z400'], [2, 'Z600'], [3, 'Z620'], [4, 'T5400'], [5, 'T5500']]
print user[1][0]
print comp[2][0]
print complist[3]