master = [None] * 100
print master[5]
for i in range(100):
	j = i*i
	master[i] = [j, j+1, j+2]

for x in range(10):
	print master[x][2]
	print master[x][1]


user = [None]
computer = [None]
seat = [None]

user = ['adam', 'toto', 'rodney', 'jon']
print user[1]
user = [[1110, 'adam'], [1111, 'toto'], [1112, 'rodney'], [1113, 'jon']]
print user[1][0]