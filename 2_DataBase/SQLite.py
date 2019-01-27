import sqlite3
import time 
import datetime
import random

#Create Table if not exists
def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS data(unix REAL, dateField TEXT, keyword TEXT, value REAL)')

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

# create_table()
# data_entry()
# read_from_db()
# update_data()
# delete_data()

c.close()
connection.close()

# for i in range(10):
# 	dynamic_data_entry()
# 	time.sleep(1)

# def dynamic_data_entry():
# 	unix = time.time()
# 	date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
# 	keyword = 'Python'
# 	value = random.randrange(0,10)
# 	c.execute("INSERT INTO data (unix, dateField, keyword, value ) VALUES (?,?,?,?)",
# 		(unix, date, keyword, value))
# 	connection.commit()



# graph_data()
# def graph_data():
# 	import matplotlib.pyplot as plt
# 	import matplotlib.dates as mdates
# 	from matplotlib import style
# 	style.use('fivethirtyeight')
# 	c.execute("SELECT unix, value FROM data")
# 	data = []
# 	values = []
# 	for row in c.fetchall():
# 		# print(datetime.datetime.fromtimestamp(row[0]))
# 		data.append(datetime.datetime.fromtimestamp(row[0]))
# 		values.append(row[1])
# 	plt.plot_date(data, values, '-')
# 	plt.show()		
