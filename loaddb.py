from seatingfuncts import *
import csv
import dircache

global alph
alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# loads/reloads the master db from files
def reloaddb():
	loaddb()
	buildrecordlist()
	initmaster()
	loadtomaster(user, 1, 0)
	loadtomaster(seat, 1, 1)
	loadseattomaster(seat, 1, 2, 2, 3)
	loadtomaster(ram, 1, 4)


# loads list into master array
def loadtomaster(name, posim, posma):
	for i in range(len(name)):
		uid = int(name[i][0])
		cont = name[i][posim]
		master[uid][posma] = cont

# loads seat list into array and swaps out number for letter
def loadseattomaster(name, posim1, posim2, posma1, posma2):
	for i in range(len(seat)):
		uid = int(seat[i][0])
		cont1 = seat[i][posim1]
		cont2 = seat[i][posim2]
		master[uid][posma1] = str(alph[int(cont1)])
		master[uid][posma2] = cont2

# prints all content of master db
def printmaster():
	for i in range(len(master)):
		print('User:'+str(i)+' - '+str(master[i]))

# saves master db back into individual lists
def savedb(name, strname):
	f = open('dbtest/'+strname, 'w')
	for i in name:
		temp = str(name[i][0])+', '+str(name[i][1])

# loads all the individual dbs into their respective lists
def loaddb():
	for each in dircache.listdir('db/'):
		reader = csv.reader(open('db/'+each, 'rb'))
		templist = []
		for record in reader:
			# print(record)
			templist.append(record)
		exec("global "+str(each)+";"+str(each)+" = templist")
		# exec("print("+str(each)+")")

# prepares the master database to be populated
def initmaster():
	global master
	master = []
	empty = '---'
	for each in dircache.listdir('db/'):
		empty = empty+'-'
	for i in range(records):
		master.append(list(empty))
		# print(range(records))

# calculates how many records to create in the master db
def buildrecordlist():
	global records
	records = 1
	for i in range(len(list(user))):
		if user[i][0] > records:
			records = user[i][0]
		records = int(records)+1


reloaddb()
printmaster()