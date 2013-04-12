master = [None] * 100
print master[5]
for i in range(100):
	j = i*i
	master[i] = [j, j+1, j+2]

for x in range(10):
	print master[x][2]
	print master[x][1]


user = [[1110, 'adam'], [1111, 'toto'], [1112, 'rodney'], [1113, 'jon']]
comp = [['adam\'s_comp', 'Z400'], ['toto\'s_Comp', 'T5500'], ['rodneyComp01' 'Z400'], ['jonbox_01', 'Z600']]
seat = [[0, 0], [0, 1], [0, 2], [1, 0]]
print user[1][0]
print comp[2][0]
