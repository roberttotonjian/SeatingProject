from seatingfuncts import *
import csv
import dircache

global alph
alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# loads/reloads the master db from files
def reloaddb():
	global listcount
	global dblist
	listcount = 0
	dblist = []
	loaddb()
	buildrecordlist()
	initmaster()
	loadtomaster(user, "user", 1, 0)
	loadtomaster(seat2, "seat1", 1, 1)
	loadtomaster(seat1, "seat2", 1, 2)
	loadtomaster(ram, "ram", 1, 3)
	loadtomaster(comp, "comp", 1, 4)


# loads list into master array
def loadtomaster(name, dbname, posim, posma):
	global listcount
	global dblist
	dblist.append(['-', '-', '-'])
	dblist[listcount][0] = dbname
	dblist[listcount][1] = posim
	dblist[listcount][2] = posma
	# dblist.append(str(dbname)+', '+str(posim)+', '+str(posma))
	for i in range(len(name)):
		uid = int(name[i][0])
		cont = name[i][posim]
		master[uid][posma] = cont
	listcount = listcount+1


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
def savedb():
	global eachdb
	global eachrec
	for eachdb in dblist:
		myfile = open("db/"+str(eachdb[0]), "w")
		myfile.write("")
		for eachrec in range(len(list(master))):
			if master[eachrec][0] != "-":
				print("-----"+str(eachrec))
				print("-----"+str(eachdb))
				dbname = eachdb[0]
				dbrec = str(master[eachrec][int(eachdb[2])])
				myfile.write(str(eachrec)+','+str(dbrec)+'\n')
				# # eachdb[0]+'.append('+str(eachrec)+','+str(master[eachrec][int(eachdb[2])]+')')
				# print("global dbname; global eachrec; global dbrec; "+str(dbname)+".append("+str(eachrec)+','+str(dbrec)+")")



# loads all the individual dbs into their respective lists
def loaddb():
	for each in dircache.listdir('db/'):
		reader = csv.reader(open('db/'+each, 'rb'))
		templist = []
		for record in reader:
			templist.append(record)
		exec("global "+str(each)+";"+str(each)+" = templist")


# prepares the master database to be populated
def initmaster():
	global master
	master = []
	empty = '---'
	for each in dircache.listdir('db/'):
		empty = empty+'-'
	for i in range(records):
		master.append(list(empty))


# calculates how many records to create in the master db
def buildrecordlist():
	global records
	records = 1
	for i in range(len(list(user))):
		if user[i][0] > records:
			records = user[i][0]
		records = int(records)+1


reloaddb()
savedb()
printmaster()