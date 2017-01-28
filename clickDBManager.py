import sqlite3
def manageDatabase(command, value = None):
	global dbName 
	global c
	global conn 
	dbName = "clicks.db" #replace with config file? 
	conn = sqlite3.connect(dbName)
	c = conn.cursor()
	c.execute('''CREATE TABLE IF NOT EXISTS clicks ("task" text, "order" text, "x" text, "y" text)''')
	if command is "add":
		addClick(value)
	elif command is "dump":
		dumpClicks()
	conn.commit()
	conn.close
def addClick(value):
	c.execute("INSERT INTO clicks VALUES (?,?,?,?)", value)
def dumpClicks():
	c.execute('select * from clicks')
	print c.fetchall()
	
