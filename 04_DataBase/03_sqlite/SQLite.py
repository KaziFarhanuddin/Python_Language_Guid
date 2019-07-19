import sqlite3

#Create Table if not exists
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS data( Personid int NOT NULL AUTO_INCREMENT, dateField TEXT, keyword TEXT, value REAL)')

#Enter
def data_entry():
	c.execute('INSERT INTO data VALUES(12, "2019-1-20", "Python", 100)')
	connection.commit()

#Read
def read_from_db():
	c.execute("SELECT * FROM data WHERE value=2 AND keyword='Python'")
	# c.execute("SELECT keyword, dateField FROM data WHERE value=2 AND keyword='Python'")
	for i in c.fetchall():
		print(i)

#Update
def update_data():
	c.execute("UPDATE data SET value=99 WHERE value=7")
	connection.commit()

#Delete
def delete_data():
	c.execute("DELETE FROM data WHERE value=99")
	connection.commit()

connection = sqlite3.connect('test.db')
c = connection.cursor()	#cursor

create_table()
data_entry()
# read_from_db()
# update_data()
# delete_data()

c.close()
connection.close()