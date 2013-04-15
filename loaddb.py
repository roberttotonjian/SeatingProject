from seatingfuncts import *
import json

# loads list into master array <name of array to impoort> <position of data in list to import> <position to import to>
def loadtomaster(name, posim, posma):
	for i in range(len(name)):
		uid = name[i][0]
		cont = name[i][posim]
		# master[uid][0] = uid
		master[uid][posma] = cont

def loadseattomaster(name, posim1, posim2, posma1, posma2):
	for i in range(len(name)):
		uid = name[i][0]
		cont1 = name[i][posim1]
		cont2 = name[i][posim2]
		master[uid][posma1] = str(alph[cont1])
		master[uid][posma2] = cont2

#prints all content of master db
def printmaster():
	for i in range(len(master)):
		print(str(i), str(master[i]))

def savedb(name, filename):
	f = open(str(filename), 'w')
	f.write(str(name))
	f.close()

# def loaddb(name, filename):
# 	f = open(str(filename), 'r')
# 	name = f.readline(0)
# 	print(name)
# 	f.close()

global alph
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
global user
user = [[1110, 'Adam'], [1111, 'Toto'], [1112, 'Rodney'], [1113, 'Jon']]
global comp
comp = [[1110, 1], [1111, 4], [1112, 3], [1113, 3]]
global seat
seat = [[1110, 1, 1], [1111, 6, 2], [1112, 4, 3], [1113, 4, 5]]
global ram
ram = [[1110, 20], [1111, 12], [1112, 8], [1113, 16]]
global complist
complist = [[0, 'Earlier Crap'], [1, 'Z400'], [2, 'Z600'], [3, 'Z620'], [4, 'T5400'], [5, 'T5500']]
global master
master = [[]]

loaddb(user, "user")

records = 1
for i in range(len(user)):
	if user[i][0] > records:
		records = user[i][0]
records = records+1
# master = str(range(records))

for i in range(records):
	master.append([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

loadtomaster(user, 1, 0)
loadtomaster(seat, 1, 1)
loadseattomaster(seat, 1, 2, 2, 3)
loadtomaster(ram, 1, 4)

# printmaster()
# savedb(user, "user")
