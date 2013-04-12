dbarray = [None] * 100
print dbarray[5]
for i in range(100):
	j = i*i
	dbarray[i] = [j, j+1, j+2]

for x in range(10):
	print dbarray[x][2]
	print dbarray[x][1]