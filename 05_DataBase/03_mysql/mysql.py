# Package installation command 
# On Fedora: "yum install MySQL-python3"

import MySQLdb

db = MySQLdb.connect("localhost", "root", "passwd@123", "Books")
cursor = db.cursor()

def GetAllBooks():
	cursor.execute("SELECT * from Books")
	data = cursor.fetchall()
	print(data)

def SearchBookName(price):
	cursor.execute("SELECT * from Books where price='%s'"%(price)) #Get database version 
	data = cursor.fetchall()
	print(data)

def SearchBookPrice(name):
	cursor.execute("SELECT * from Books where name='%s'"%(name)) #Get database version 
	data = cursor.fetchall()
	print(data)

def PutBook(name, price):
	cursor.execute("INSERT INTO Books values(%s, %s)",(name,price)) #Get database version 
	db.commit()

while True:
	option = int(input("\tSQL\n1.See all data\n2.Put Data\n3.Search by Name\n4.Search by Price\n"))
	if option == 1:
		GetAllBooks()

	elif option == 2:
		name =input("Enter Name of Book : ")
		price = input("Enter Price of Book : ")
		PutBook(name, price)
	elif option == 3:
		name = input("Eter Name : ")
		SearchBookPrice(name)
	elif option == 4:
		price = input("Eter Price : ")
		SearchBookName(price)

	else:
		break


db.close()
