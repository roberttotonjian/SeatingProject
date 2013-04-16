from seatingfuncts import *
import csv

global alph
global user
global comp
global seat
global ram
global complist
global master
global dblist

alph = []
user = []
comp = []
seat = []
ram = []
complist = []
dblist = []
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
master = [[]]


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
		print('User:'+str(i)+' - '+str(master[i]))

def savedb(name, strname):
	f = open('db/'+strname, 'w')
	for i in name:
		temp = str(name[i][0])+', '+str(name[i][1])

def loaddblist():
	reader = csv.reader(open('db/list', 'rb'))
	for record in reader:
		record = str(record).replace("[", "")
		record = str(record).replace("]", "")
		record = str(record).replace("'", "")
		record = str(record).replace("'", "")
		dblist.append(record)


def loaddb():
	for each in dblist:
		reader = csv.reader(open('db/'+each, 'rb'))
		for record in reader:
			# print(record)
			user.append(record)

# user = [[1110, 'Adam'], [1111, 'Toto'], [1112, 'Rodney'], [1113, 'Jon']]
# comp = [[1110, 1], [1111, 4], [1112, 3], [1113, 3]]
# seat = [[1110, 1, 1], [1111, 6, 2], [1112, 4, 3], [1113, 4, 5]]
# ram = [[1110, 20], [1111, 12], [1112, 8], [1113, 16]]
# complist = [[0, 'Earlier Crap'], [1, 'Z400'], [2, 'Z600'], [3, 'Z620'], [4, 'T5400'], [5, 'T5500']]


loaddblist()
loaddb()

print(dblist)

print(user)

# for db in list(dblist):
# 	print db
# 	f = open('db/'+str(db), 'r')
# 	db = [item.strip('\n') line.split(',') for line in open('db/'+str(db))]
# 	f.close()




# records = 1
# for i in range(len(list(user))):
# 	if user[i][0] > records:
# 		records = user[i][0]
# records = records+1
# # master = str(range(records))

# for i in range(records):
# 	master.append([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None])

# loadtomaster(user, 1, 0)
# loadtomaster(seat, 1, 1)
# loadseattomaster(seat, 1, 2, 2, 3)
# loadtomaster(ram, 1, 4)


# printmaster()











